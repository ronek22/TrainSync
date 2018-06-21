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
from selenium.webdriver.common.keys import Keys


# TODO refactor this file, so it can be a class

def clickable(waitDriver, xpath):
    element = waitDriver.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()

def login():
    # receive login data
    f = open('client.secret').readlines()
    userEnd, passwdEnd = f[1].strip().split(',')

    browser.get("https://www.endomondo.com/login")
    mail = wait.until(EC.element_to_be_clickable((By.NAME, 'email')))
    mail.send_keys(userEnd)

    pswd = wait.until(EC.element_to_be_clickable((By.NAME, 'password')))
    pswd.send_keys(passwdEnd)
    pswd.submit()

def checkNewWorkout():
    count = files.countTcx()
    if count == 0:
        print("Brak plikow do importu")
        exit(1)
    return count

def redirectToAddWorkoutPage():
    element = wait.until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[2]/header/div[3]/ul/li[6]/a')))
    element.send_keys(Keys.RETURN)

    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'fileImport')))
    element.click()


    browser.switch_to_default_content()
    wait.until(EC.frame_to_be_available_and_switch_to_it(
        (By.CLASS_NAME, 'iframed')))

def uploadDownloadedWorkouts():
    i = 0
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

def finish():
    browser.quit()
    print("Importowanie powiodlo sie")
    files.delTcx()

browser = webdriver.Firefox()
wait = WebDriverWait(browser, 60)
count = checkNewWorkout()

login()
redirectToAddWorkoutPage()
uploadDownloadedWorkouts()
finish()
