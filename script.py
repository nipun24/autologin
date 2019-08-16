import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()

driver.get("http://172.16.16.16:8090")

username = driver.find_element_by_name('username')
username.send_keys('student')

password = driver.find_element_by_name('password')
password.send_keys('student')

submit = driver.find_element_by_name('btnSubmit')
submit.click()