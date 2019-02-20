import time
from selenium import webdriver
import secrets

driver = webdriver.Chrome() 
driver.get('http://www.facebook.com')
email = driver.find_element_by_name('email')
email.send_keys(secrets.email)
password = driver.find_element_by_name('pass')
password.send_keys(secrets.password)
password.submit()
driver.get('http://www.facebook.com/events/birthdays')
birthday = driver.find_elements_by_xpath("//*[@placeholder[contains(., 'Write a birthday wish')]]")
birthday[0].send_keys('Happy Birthday!!')
time.sleep(5)

driver.quit()