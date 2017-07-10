import mechanize
import sys
import re
import getpass

def toHTML(res, name):
	name = name + '.html'
	with open(name, 'w') as f:
		f.write(res.read())

reload(sys)
sys.setdefaultencoding('utf-8')
br = mechanize.Browser()

# some useful base string
baseURL = 'https://www.strava.com'

userStr = raw_input("Podaj email: ")
passStr = getpass.getpass("Podaj haslo: ")

response = br.open('https://strava.com/login')
br.select_form(nr=0)


br.form['email'] = userStr
br.form['password'] = passStr

response = br.submit()

if br.geturl() == 'https://www.strava.com/dashboard':
	print "Logowanie udane"

	response == br.open('https://www.strava.com/athlete/training')
	ile = int(raw_input("Ile aktywnosci chcesz pobrac? (max = 10)"))
	i = 0
	for link in br.links(url_regex="^\/activities\/\d{1,10}$"):
		if i == ile:
			break

		tcx = baseURL+link.url+'/export_tcx'
		print "Pobieram "+str(i+1)+" aktywnosc"
		t = br.retrieve(tcx, str(i)+'.tcx')
		i += 1

	# remove.delTcx()



else:
	print "Logowanie nie udane"
	exit(1)
