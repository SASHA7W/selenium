import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
download_path = os.path.join(os.getcwd(), "/data/selenium/lesson10/downloads")

if not os.path.exists(download_path):
    os.makedirs(download_path)
preferences = {"download.default_directory": download_path}
options.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome(service=service, options=options)

driver.get ("https://demoqa.com/upload-download")
download_button = driver.find_element("xpath", "//a[@id = 'downloadButton']")
download_button.click()
time.sleep(3)
driver.quit()