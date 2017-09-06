import mechanize
import sys
import re
import getpass
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def toHTML(res, name):
	name = name + '.html'
	with open(name, 'w') as f:
		f.write(res.read())

reload(sys)
sys.setdefaultencoding('utf-8')
br = mechanize.Browser()

# some useful base string
baseURL = 'https://www.flow.polar.com'

ile = int(raw_input("Ile aktywnosci chcesz pobrac? (max = 10)\n>> "))
cls()
# userStr,passStr =  open('client.secret').readline().strip().split(',')
userStr = "kuba.ronkiewicz@live.com"
passStr = "Wbmjmka96"
# userStr = raw_input("Podaj email: ")
# passStr = getpass.getpass("Podaj haslo: ")

response = br.open('https://flow.polar.com/login')
br.select_form(nr=0)


br.form['email'] = userStr
br.form['password'] = passStr

response = br.submit()
print '{:~^30}'.format('Polar')
print br.geturl()

if br.geturl() == 'https://flow.polar.com/':
    print "Logowanie udane"
    response == br.open('https://flow.polar.com/diary')
    print br.geturl()
	# i = 0
    for link in br.links():
        print link.url
	# 	if i == ile:
	# 		break
	# 	tcx = baseURL+link.url+'/export_tcx'
	# 	print "Pobieram "+str(i+1)+" aktywnosc..."
	# 	t = br.retrieve(tcx, str(i)+'.tcx')
	# 	print "Pobrane"
	# 	i += 1

    br.close()

else:
	print "Logowanie nie udane"
	exit(1)
