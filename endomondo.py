# -*- coding: utf-8 -*-
import sys
import os
import files
import getpass
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def clickable(waitDriver, xpath):
    element = waitDriver.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()


count = files.countTcx()
if count == 0:
    print("Brak plikow do importu")
    exit(1)

f = open('client.secret').readlines()
userEnd, passwdEnd = f[1].strip().split(',')


browser = webdriver.Firefox()
# browser.set_window_position(-3000, 0)
wait = WebDriverWait(browser, 60)

browser.get("https://www.endomondo.com/?language=EN")
link = browser.find_element_by_class_name('header-guest-login-link')
link.click()


mail = wait.until(EC.element_to_be_clickable((By.NAME, 'email')))
mail.send_keys(userEnd)

pswd = wait.until(EC.element_to_be_clickable((By.NAME, 'password')))
pswd.send_keys(passwdEnd)

submit = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[contains(text(),'Log In')]")))
submit.click()

# url = wait.until(EC.url_to_be(url='https://www.endomondo.com/home'))
# print('{:~^30}'.format('Endomondo'))
# if not url:
#    print("Logowanie nie udane")
#    files.delTcx()
#    browser.quit()
#    exit(-1)
# print("Logowanie udane")
i = 0


clickable(wait, 'html/body/div[2]/header/div[3]/ul/li[6]/a')

element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'fileImport')))
element.click()


browser.switch_to_default_content()
wait.until(EC.frame_to_be_available_and_switch_to_it(
    (By.CLASS_NAME, 'iframed')))


while i < count:
    print("Importowanie pliku nr %d..." % i)
    pwd = os.getcwd() + "\\" + str(i) + ".tcx"
    element = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//form/div[2]/div[2]/input')))
    element.send_keys(pwd)
    clickable(
        wait, "//div[contains(@class,'navigation')]/a[contains(@id,'id11')]")
    if i == count - 1:
        clickable(
            wait, "//div[contains(@class,'navigation')]/a[contains(@id,'id14')]")
    else:
        clickable(
            wait, "//div[contains(@class,'navigation')]/a[contains(@id,'id15')]")
    i += 1


browser.quit()
print("Importowanie powiodlo sie")
files.delTcx()
