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

# easymode

Easy= browser.find_element_by_partial_link_text("Easy")
Easy.click()


browser.implicitly_wait(10000)
#Show hint

showhint = browser.find_element_by_partial_link_text("Show A Hint")
showhint.click()

browser.implicitly_wait(10000)
# Verify solution  

verifysolution = browser.find_element_by_partial_link_text("Verify Solution")
verifysolution.click()

browser.implicitly_wait(10000)
#pause

pause = browser.find_element_by_partial_link_text("Pause")

pause.click()

browser.implicitly_wait(10000) 

#Resume

Resume = browser.find_element_by_partial_link_text("Resume")
Resume.click()

browser.implicitly_wait(10000)
#Display solution 

Displaysolution = browser.find_element_by_partial_link_text("Display Solution")

Displaysolution.click()

browser.implicitly_wait(10000)
#newgame

newgame = browser.find_element_by_partial_link_text("New Game")
newgame.click()

browser.implicitly_wait(10000)
#sudoku

sudoku = browser.find_element_by_xpath("/html/body/nav/div/div[1]/a/img")

sudoku.click()



