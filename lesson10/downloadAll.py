import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
download_path = os.path.join(os.getcwd(), "/data/selenium/lesson10/downloads")

if not os.path.exists(download_path):
    os.makedirs(download_path)
preferences = {"download.default_directory": download_path}
options.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://the-internet.herokuapp.com/download")
driver.find_elements("xpath", "//div/a[contains(@href,'download')]")
for element in driver.find_elements("xpath", "//div/a[contains(@href,'download')]"):
    element.click()
    time.sleep(1)