from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By
from keys import fglogin, fgpassword
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

wait = random.randint(3, 5)
waitLonger = random.randint(7, 10)

workUsername = fglogin
workPassword = fgpassword

#login
service = webdriver.ChromeService()
driver = webdriver.Chrome()
driver.get('https://www.fieldglass.net/')
driver.implicitly_wait(wait)
username = driver.find_element(By.ID, "usernameId_new")
driver.implicitly_wait(wait)
username.send_keys(workUsername)
password = driver.find_element(By.ID, "passwordId_new")
driver.implicitly_wait(wait)
password.send_keys(workPassword)
driver.implicitly_wait(wait)
login = driver.find_element(By.NAME, 'action').click()
driver.implicitly_wait(waitLonger)

#Create and fill in Expense Sheet
expenseSheet = driver.find_element(By.ID, "tile_999").click()
driver.implicitly_wait(wait)
content = driver.find_element(By.CLASS_NAME, 'content').click
driver.implicitly_wait(waitLonger)

#all_title = driver.find_elements_by_class_name("title")
#title = [title.text for title in all_title]
#print(title)