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


userEnd = raw_input("Podaj email: ")
passwdEnd = getpass.getpass("Podaj haslo: ")


browser = webdriver.Firefox()

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

sleep(5)
if browser.current_url != "https://www.endomondo.com/home":
    print "Logowanie nie udane"
    files.delTcx()
    browser.quit()
    exit(-1)
print "Logowanie udane"

# wait until load
sleep(10)
i = 0

while i<count:

    browser.find_element_by_xpath('html/body/div[2]/header/div[3]/ul/li[6]/a').click()
    print "Importowanie pliku nr %d" % i

    browser.find_element_by_class_name('fileImport').click()
    print "Import"
    browser.switch_to_default_content()

    frame = browser.find_element_by_class_name('iframed')
    browser.switch_to_frame(frame)
    sleep(5)
    pwd = os.getcwd()+"\\"+str(i)+".tcx"
    browser.find_element_by_xpath('//form/div[2]/div[2]/input').send_keys(pwd)
    sleep(5)
    browser.find_element_by_xpath("//div[contains(@class,'navigation')]/a").click()
    sleep(7)
    browser.find_element_by_xpath("//div[contains(@class,'navigation')]/a[2]").click()
    sleep(5)
    browser.switch_to_default_content()
    i+=1
    sleep(5)
    print "UKONCZONO"

browser.quit()
files.delTcx()
