import mechanize
import sys
from os import remove
import re
from glob import glob
from bs4 import BeautifulSoup

def toHTML(res, name):
	name = name + '.html'
	with open(name, 'w') as f:
		f.write(res.read())

reload(sys)
sys.setdefaultencoding('utf-8')
br = mechanize.Browser()

# some useful base string
baseURL = 'https://www.strava.com'

response = br.open('https://strava.com/login')
br.select_form(nr=0)

email = raw_input("Podaj e-mail: ")
haslo = raw_input("Podaj haslo: ")

br.form['email'] = email
br.form['password'] = haslo

response = br.submit()

if br.geturl() == 'https://www.strava.com/dashboard':
	print "Logowanie sie powiodlo"
	"""
	with open('st.html', 'w') as f:
		f.write(response.read())
	"""

	response == br.open('https://www.strava.com/athlete/training')

	to_download = []
	ile = int(raw_input("Ile aktywnosci chcesz pobrac?"))

	i = 0
	for link in br.links():
		if i == ile:
			break

		x=re.match(r'^\/activities\/\d{1,10}$', link.url)

		if str(x) != 'None':
			tcx = baseURL+link.url+'/export_tcx'
			print "Pobieram "+str(i+1)+" aktywnosc"
			t = br.retrieve(tcx, str(i)+'.tcx')
			i += 1

	os.remove(glob('*.tcx'))


else:
	print "Logowanie nie udane"
