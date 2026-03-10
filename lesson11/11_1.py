from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 30, poll_frequency=1)

driver.get ("https://omayo.blogspot.com/")

VISIBLE_TEXT = ("xpath", "//div[contains(@id, 'deletesuccess')]")
wait.until(EC.invisibility_of_element_located(VISIBLE_TEXT))
print("Element invisible")