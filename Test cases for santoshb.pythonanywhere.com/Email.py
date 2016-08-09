from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import Select 
import time
import random

#ran = random.randint(1,50) 
#ran1 = "test+@ran"
#print ran1

#Navigate to chrome
options = webdriver.ChromeOptions() 
options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=options) 

#Goto to browser 
browser.get("http://fusion.kentsudoku.com/")  

assert "Fusion" in browser.title

browser.implicitly_wait(20) 

#Login

Emailid = browser.find_element_by_name("inputEmail")
Emailid.send_keys("test@gmail.com")


Password = browser.find_element_by_name("inputPassword")
Password.send_keys("Secure*12")

login = browser.find_element_by_xpath("//*[@id='navbar']/form/button")
login.click()

