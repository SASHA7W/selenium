from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
import pickle

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")
wikipedia = driver.find_element(By.CLASS_NAME, "wikipedia-icon").click()
time.sleep(5)
print("Wiki", wikipedia)
