from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
url='https://outlook.live.com/owa/'
driver=webdriver.Chrome("/Users/Jorge/Downloads/chromedriver_win32/chromedriver")
driver.get(url)
time.sleep(3)
driver.find_element_by_class_name('linkButtonSigninHeader').click()
time.sleep(4)
nombre='Usernamenumber'+str(random.randrange(1000000))
driver.find_element_by_id('MemberName').send_keys(nombre)
time.sleep(3)
driver.find_element_by_id("iSignupAction").click()
time.sleep(3)
driver.find_element_by_id('PasswordInput').send_keys('Soyundios')
time.sleep(4)
driver.find_element_by_id("iSignupAction").click()
time.sleep(3)
driver.find_element_by_id("FirstName").send_keys('User')
time.sleep(3)
driver.find_element_by_id('LastName').send_keys('LastName')
time.sleep(3)
driver.find_element_by_id("iSignupAction").click()
time.sleep(3)
driver.find_element_by_id('BirthDay').click()
time.sleep(3)
driver.find_element_by_id('BirthDay').send_keys('1')
time.sleep(2)
driver.find_element_by_id('BirthMonth').send_keys('julio')
time.sleep(2)
driver.find_element_by_id('BirthYear').send_keys('1999')
time.sleep(2)
driver.find_element_by_id("iSignupAction").click()