import time
from selenium import webdriver
from secrets import email, password

driver = webdriver.Chrome() 
driver.get('http://www.facebook.com')
e = driver.find_element_by_name('email')
e.send_keys(email)
p = driver.find_element_by_name('pass')
p.send_keys(password)
p.submit()
driver.get('http://www.facebook.com/events/birthdays')
birthdays = driver.find_elements_by_xpath("//*[@placeholder[contains(., 'Write a birthday wish')]]")
for birthday in birthdays:
    birthday.send_keys('Happy Birthday!!')
    
time.sleep(5)

driver.quit()