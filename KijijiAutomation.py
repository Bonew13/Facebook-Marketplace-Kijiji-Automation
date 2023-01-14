from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys
sys.tracebacklimit = 0

#Opening Username and Password file for Kijiji
with open(r"YOUR DIRECTORY HERE\\Kijiji and Facebook Marketplace automation\\Passwords and Usernames\\passuserkijiji.txt", encoding="utf-8") as f:
    user, passw = f.read().splitlines()

f.closed


#Path to Chrome Drivera
PATH = "YOUR DIRECTORY HERE\chromedriver.exe"

##Enabling Stealth Mode
options = Options()
options.add_argument("disable-blink-features=AutomationControlled") #Disables Chrome's Automation Control 
driver = webdriver.Chrome(executable_path= PATH, options=options)

##Opening Kijiji
driver.get("https://www.kijiji.ca/p-select-category.html")
time.sleep(1)

##Logging In
driver.find_element(By.ID, 'emailOrNickname').send_keys(user)
driver.find_element(By.ID, 'password').send_keys(passw)
driver.find_element(By.XPATH, '//*[@id="LoginForm"]/button').click()
time.sleep(5)

#Title and category
driver.find_element(By.ID, 'AdTitleForm').send_keys("Keyboard for Sale")
driver.find_element(By.XPATH, '//*[@id="mainPageContent"]/div/div/div/div[2]/div/div/div[2]/div[1]/div/button').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="CategorySuggestion"]/div/ul/li[1]/button').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="CategorySuggestion"]/div/ul[2]/li[10]/button').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="CategorySuggestion"]/div/ul[2]/li[1]/button').click()
driver.find_element(By.XPATH, '//*[@id="desktopbrand_s"]').click()
time.sleep(1)
driver.find_element(By.ID, 'pstad-descrptn').send_keys("Keyboard for Sale\nGreat Condition\nPick up in XYZ")
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="html5_1gmcq366r1n721pl69571qiaepq3"]').send_keys(r"YOUR DIRECTORY HERE\\Kijiji and Facebook Marketplace automation\\Photos\\UploadPhoto1.jpg")
driver.find_element(By.ID, 'PriceAmount').send_keys("55")


time.sleep(1)

time.sleep(10)