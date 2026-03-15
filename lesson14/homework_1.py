from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import pickle

download_path = os.path.join(os.getcwd(), "/data/selenium/lesson14")
options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://chromewebstore.google.com/category/extensions/lifestyle/shopping")
driver.add_cookie({'name': "username", 'value': "user123"})
driver.refresh()
cookie_username = driver.get_cookie("username")
print(cookie_username)
allCookies = driver.get_cookies()
time.sleep(5)
driver.delete_cookie()
driver.refresh()
time.sleep(5)
driver.add_cookie(allCookies)
driver.refresh()
