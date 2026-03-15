from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle

options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://chromewebstore.google.com/category/extensions/lifestyle/shopping")
some_cookie = driver.get_cookie("__Secure-3PAPISID")
print(some_cookie)
driver.delete_cookie("__Secure-3PAPISID")
driver.refresh()
print("Cookie was not found", some_cookie)