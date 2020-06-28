from selenium import webdriver 
from time import sleep

usr = input('Enter email address')
pwd = input('Enter password')
driver = webdriver.Firefox()
driver.get('https://www.facebook.com/')
print("Opened facebook")
username_box=driver.find_element_by_id('email')
username_box.send_keys(usr)
password_box=driver.find_element_by_id('password')
password_box.send_keys(pwd)
login_box=driver.find_element_by_id('login')
login_box.click()

driver.quit()


