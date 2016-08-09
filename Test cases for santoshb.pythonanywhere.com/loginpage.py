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

#Login button

login = browser.find_element_by_xpath("/html/body/div[3]/div/div/p[2]/a[1]")

login.click()

# Email

email = browser.find_element_by_id("inputEmail")

email.send_keys("test@gmail.com")

# Password

password = browser.find_element_by_id("inputPassword")

password.send_keys("Secure*12")


# Submit

submit = browser.find_element_by_xpath("/html/body/div[3]/div/div/form/button")

submit.click()

