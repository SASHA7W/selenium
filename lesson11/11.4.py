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
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get ("https://omayo.blogspot.com/")

BUTTON_TRY_IT = driver.find_element("xpath", "//button[contains(., 'Try it')]")
BUTTON_TRY_IT.click()
print("The click on the button is performed")

DISABLED_BUTTON = ("xpath", "//button[contains(@id, 'btn') or @disabled]")
wait.until(EC.presence_of_element_located(DISABLED_BUTTON))
time.sleep(7)
print("The button is disabled now")