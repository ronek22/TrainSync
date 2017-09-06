# -*- coding: utf-8 -*-
import sys
import os
import files
import getpass
from time import sleep
from selenium import webdriver


reload(sys)
sys.setdefaultencoding('utf-8')

count = files.countTcx()
if count == 0:
    print "Brak plikow do importu"
    exit(1)



f = open('client.secret').readlines()
userEnd,passwdEnd = f[1].strip().split(',')

browser = webdriver.Firefox()
browser.set_window_position(-3000,0)
browser.get("https://www.endomondo.com/?language=EN")
link = browser.find_element_by_class_name('header-guest-login-link')
link.click()


sleep(3)
mail = browser.find_element_by_name('email')
pswd = browser.find_element_by_name('password')
submit = browser.find_element_by_xpath("//button[contains(text(),'Log In')]")
mail.send_keys(userEnd)
pswd.send_keys(passwdEnd)
submit.click()

print '{:~^30}'.format('Endomondo')
sleep(5)
if browser.current_url != "https://www.endomondo.com/home":
    print "Logowanie nie udane"
    files.delTcx()
    browser.quit()
    exit(-1)
print "Logowanie udane"

# wait until load
sleep(5)
i = 0

while i<count:

    browser.find_element_by_xpath('html/body/div[2]/header/div[3]/ul/li[6]/a').click()
    print "Importowanie pliku nr %d..." % i

    browser.find_element_by_class_name('fileImport').click()
    browser.switch_to_default_content()
    sleep(7)
    frame = browser.find_element_by_class_name('iframed')
    browser.switch_to_frame(frame)
    sleep(7)
    pwd = os.getcwd()+"\\"+str(i)+".tcx"
    browser.find_element_by_xpath('//form/div[2]/div[2]/input').send_keys(pwd)
    sleep(7)
    browser.find_element_by_xpath("//div[contains(@class,'navigation')]/a").click()
    print "Wrzucone"
    sleep(10)
    browser.find_element_by_xpath("//div[contains(@class,'navigation')]/a[2]").click()
    print "Zapisane"
    # sleep(5)
    browser.switch_to_default_content()
    i+=1
    sleep(5)
    print "Done\n"

browser.quit()
files.delTcx()
