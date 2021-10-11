#!/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from os import listdir
from os.path import isfile, join
import sys

def upload_file(driver,file,location):
    driver.get("https://2021.igem.org/Special:Upload")
    uploadbutton = driver.find_element_by_id("wpUploadFile")
    uploadbutton.send_keys(location+"/"+file)
    name = driver.find_element_by_id("wpDestFile")
    name.send_keys("T--TU_Kaiserslautern--"+file)
    sleep(3)
    upld = driver.find_element_by_name("wpUpload")
    upld.click()
    sleep(4)
def login():
    driver = webdriver.Firefox()
    driver.get("https://2021.igem.org/Special:Upload")
    driver.implicitly_wait(20)
    login = driver.find_element_by_id("user_item")
    print("found")
    sleep(1)
    print("done")
    login.click()
    driver.switch_to_frame(driver.find_element_by_id('nlogin_iframe'))
    user = driver.find_element_by_xpath("/html/body/form/div[1]/input[1]")
    password = driver.find_element_by_xpath("/html/body/form/div[1]/input[2]")
    login = driver.find_element_by_name("Login")
    user.send_keys("julest")
    password.send_keys("igemkljules69")
    login.click()
    sleep(3)
    return driver
def getLinks(driver):
    driver.get("https://2021.igem.org/Special:ListFiles")
    limit = driver.find_element_by_id("mw-input-limit")
    search = driver.find_element_by_id("mw-listfiles-user")
    go = driver.find_element_by_class_name("mw-htmlform-submit")
    search.send_keys("julest")
    Select(limit).select_by_value('500')
    sleep(0.1)
    go.click()
    sleep(2)
    links = driver.find_elements_by_link_text("file")
    res =(list(map(lambda x: x.get_attribute("href"),links)))
    driver.close()
    return res;
def doUp(location):
    driver = login()
    files = [f for f in listdir(location) if isfile(join(location, f))]
    flag = False
    for file in files:
        if(True):
            try:
                upload_file(driver,file,location)
            except KeyboardInterrupt:
                flag = False
        else:
            break
        print(f"{file} uploaded!")
    print("Done!")
    driver.close()
def doLinks():
    driver = login()
    return getLinks(driver)
if __name__ == "__main__":
    if(len(sys.argv)>1):
        doUp(sys.argv[1])

