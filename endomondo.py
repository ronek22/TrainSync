# -*- coding: utf-8 -*-
import sys
import os
from time import sleep
from selenium import webdriver

reload(sys)
sys.setdefaultencoding('utf-8')


browser = webdriver.PhantomJS()
browser.set_window_size(1124, 850)

browser.get("https://www.endomondo.com/?language=EN")
browser.save_screenshot('1.png')
link = browser.find_element_by_class_name('header-guest-login-link')
link.click()
browser.save_screenshot('2.png')

#user = raw_input("Podaj email: ")
#passwd = raw_input("Podaj haslo: ")
sleep(3)
user = 'kuba.ronkiewicz@live.com'
passwd = 'ronaldo22'
mail = browser.find_element_by_name('email')
pswd = browser.find_element_by_name('password')
submit = browser.find_element_by_xpath("//button[contains(text(),'Log In')]")
mail.send_keys(user)
pswd.send_keys(passwd)
browser.save_screenshot('3.png')
submit.click()
print "Logowanie udane"

browser.save_screenshot('dupa.png')
# wait until load
sleep(10)

submit = browser.find_element_by_xpath('html/body/div[2]/header/div[3]/ul/li[6]/a')
submit.click()
print "Dodawanie"

browser.find_element_by_class_name('fileImport').click()
print "Import"
browser.switch_to_default_content()
frame = browser.find_element_by_class_name('iframed')
browser.switch_to_frame(frame)
sleep(5)
browser.save_screenshot('error.png')
browser.find_element_by_xpath('//form/div[2]/div[2]/input').send_keys(os.getcwd()+"\\0.tcx")
browser.find_element_by_xpath("//div[contains(@class,'navigation')]/a").click()
sleep(3)
browser.find_element_by_xpath("//div[contains(@class,'navigation')]/a[2]").click()
sleep(3)
browser.switch_to_default_content()
browser.find_element_by_xpath('html/body/div[2]/header/div[3]/ul/li[6]/a').click()
print "UKONCZONO"
browser.quit()
# browser.switch_to_frame(2)
# browser.find_element_by_name('uploadFile')
# .send_keys(os.getcwd()+"0.tcx")
