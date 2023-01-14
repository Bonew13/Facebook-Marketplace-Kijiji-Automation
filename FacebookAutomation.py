from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys
sys.tracebacklimit = 0

#Opening Username and Password file
with open(r"YOUR DIRECTORY HERE\\Kijiji and Facebook Marketplace automation\\Passwords and Usernames\\passuserfb.txt", encoding="utf-8") as f:
    user, passw = f.read().splitlines()

f.close


#Path to Chrome Drivera
PATH = "C:\Program Files (x86)\chromedriver.exe"

##Disabling notifcations
options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
driver = webdriver.Chrome(executable_path=PATH, options=options) 

##Opening Facebook and Logging in
driver.get("https://www.facebook.com")
username = driver.find_element(By.ID, "email").send_keys(user)
password = driver.find_element(By.ID, "pass").send_keys(passw)
driver.find_element(By.NAME, "login").click()
time.sleep(1)
driver.get("https://www.facebook.com/marketplace/create/item")  
time.sleep(1)

##Creating Ad
driver.find_element(By.XPATH, "//span[text()='Title']//following::input[1]" ).send_keys("Keyboard for Sale")
driver.find_element(By.XPATH, "//span[text()='Price']//following::input[1]" ).send_keys("55")
driver.find_element(By.XPATH, "//*[text()='Category']//following::i[1]").click()
driver.find_element(By.XPATH, "//span[text()='Electronics & computers']").click()
driver.find_element(By.XPATH, "//*[text()='Condition']//following::i[1]").click()
driver.find_element(By.XPATH, "//span[text()='Used - Good']").click()
driver.find_element(By.XPATH, "//span[text() = 'Description']//following::textarea[1]" ).send_keys("Keyboard for Sale\nGreat Condition\nPick up in XYZ ")
driver.find_element(By.XPATH, "//input[contains(@accept,'image') and @type='file']" ).send_keys(r"YOUR DIRECTORY HERE\\Kijiji and Facebook Marketplace automation\\Photos\\UploadPhoto1.jpg")
driver.find_element(By.XPATH, "//span[text()='Next']").click()
time.sleep(3)

##Publish
#driver.find_element(By.XPATH, "//div[@aria-label='Publish']").click()
