from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#ENTER LINKEDIN USERNAME/PASSWORD
ACCOUNT_EMAIL = "YOUREMAIL"
ACCOUNT_PASSWORD = "YOURPASSWORD"

driver.get("https://www.linkedin.com")

#Wait for the page to load.
time.sleep(5)

email_field = driver.find_element(By.XPATH,"//*[@id='session_key']")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.XPATH,'//*[@id="session_password"]')
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)
