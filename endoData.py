import requests
import platform
import uuid
import socket
import json

__title__ = 'strava2endomondo'
__version__ = '0.5'
URL_AUTHENTICATE = 'https://api.mobile.endomondo.com/mobile/auth'
URL_WORKOUTS = 'https://api.mobile.endomondo.com/mobile/api/workouts'
URL_WORKOUT_GET = 'https://api.mobile.endomondo.com/mobile/api/workout/get'
URL_WORKOUT_POST = 'https://api.mobile.endomondo.com/mobile/api/workout/post'
URL_TRACK = 'https://api.mobile.endomondo.com/mobile/track'
URL_PLAYLIST = 'https://api.mobile.endomondo.com/mobile/playlist'

URL_ACCOUNT_GET = 'https://api.mobile.endomondo.com/mobile/api/profile/account/get'
URL_ACCOUNT_POST = 'https://api.mobile.endomondo.com/mobile/api/profile/account/post'

UNITS_METRIC = 'METRIC'
UNITS_IMPERIAL = 'IMPERIAL'

GENDER_MALE = 'MALE'
GENDER_FEMALE = 'FEMALE'
last = None


class EndoApi(object):
    auth_token = None
    secure_token = None
    Requests = requests.session()

    device_info = {
        'os':			platform.system(),
        'model':		platform.python_implementation(),
        'osVersion':	platform.release(),
        'vendor':		'github/ronek22',
        'appVariant':	__title__,
        'country':		'PL',
        'v':			'2.4',  # No idea, maybe api version?
        'appVersion':	__version__,
        'deviceId':		str(uuid.uuid5(uuid.NAMESPACE_DNS, socket.gethostname())),
    }

    def __init__(self, **kwargs):
        '''
                :param auth_token: Optional Previous authentication token to use.
                :param email: Optional Authentication email.
                :param password: Optional Authentication password.
        '''
        email = kwargs.get('email')
        password = kwargs.get('password')

        if kwargs.get('auth_token'):
            self.set_auth_token(kwargs.get('auth_token'))
        elif email and password:
            self.set_auth_token(self.request_auth_token(email, password))

        if self.device_info['os'] in ['Linux']:
            self.device_info['vendor'] = platform.linux_distribution()[0]

        self.Requests.headers['User-Agent'] = '{appVariant}/{appVersion} ({os}; {osVersion}; {model}) {vendor}'.format(
            **self.device_info)

    def get_auth_token(self):
        return self.auth_token

    def set_auth_token(self, auth_token):
        self.auth_token = auth_token

    def request_auth_token(self, email, password):
        params = self.device_info
        params.update({
            'action':	'pair',
            'email':	email,
            'password':	password
        })

        r = self.Requests.get(URL_AUTHENTICATE, params=params)

        lines = r.text.split("\n")
        # print lines
        if lines[0] != "OK":
            logging.warning(
                "Logging failed into Endomondo, returned data was: %s" % r.text)
            raise AuthenticationError(
                "Could not authenticate with Endomondo, Expected 'OK', got '%s'" % lines[0])

        lines.pop(0)
        # print lines
        for line in lines:
            key, value = line.split("=")
            if key == "authToken":
                return value
        return False

    def make_request(self, url, params={}, method='GET', data=None, **kwargs):
        params.setdefault('authToken', self.auth_token)
        params.setdefault('language', 'en')

        # Flatten 'fields'
        if type(params.get('fields')) is list:
            params['fields'] = ','.join(params['fields'])

        if data and params.get('gzip') == 'true':
            data = gzip_string(data)
        elif data and params.get('deflate') == 'true':
            data = zlib.compress(data)

        r = self.Requests.request(
            method, url, data=data, params=params, **kwargs)

        if r.status_code != requests.codes.ok:
            logging.debug('Endomondo returned failed status code. Code: %s, message: %s' % (
                r.status_code, r.text))

        r.raise_for_status()

        try:
            data = r.json()
            if data.has_key('error'):
                logging.warning(
                    'Error loading data from Endomondo. Type: %s', data['error'].get('type'))
                err_type = data['error'].get('type')
                if err_type == 'AUTH_FAILED':
                    raise AuthenticationError(
                        'Authentication token was not valid.')
        except:
            '''pass'''
        return r

    def last_workout(self, before=None, **kwargs):
        kwargs.setdefault('maxResults', 20)
        # Default fields used by Endomondo 10.1 App
        kwargs.setdefault('fields', ['device', 'simple', 'basic', 'lcp_count'])

        # Flatten 'before'
        if before != None:
            if isinstance(before, datetime):
                kwargs['before'] = datetime_to_str(before)
            elif type(before) is str:
                kwargs['before'] = before
            else:
                raise ValueError(
                    "Param 'before' needs to be datetime object or iso formatted string.")

        if kwargs.get('deflate') == 'true':
            kwargs.setdefault('compression', 'deflate')

        r = self.make_request(URL_WORKOUTS, kwargs)

        workouts = []

        return r.json().get('data', [])[0]['start_time']


def run():
    auth = None
    f = open('client.secret','a+')
    line = f.readlines()
    try:
        auth = line[3]
    except IndexError:
        userEnd,passwdEnd = line[1].strip().split(',')

    if not auth:
        endo = EndoApi(email="jronek3010@gmail.com", password="Wbmjmka96")
        auth = endo.get_auth_token()
        f.write(auth)
        f.close()
    else:
        endo = EndoApi(auth_token=auth)
    last = endo.last_workout()[:10]
    return last
