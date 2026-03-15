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
time.sleep(2)

print(driver.get_cookies())

driver.delete_all_cookies()
driver.add_cookie({'name': 'test_cookie', 'value': 'test_value'})
before = driver.get_cookie("test_cookie")
print("Before", before)
driver.delete_cookie("test_cookie")

driver.add_cookie({'name': 'paramon', 'value': 'test_value'})
after = driver.get_cookie("paramon")
print("After", after)