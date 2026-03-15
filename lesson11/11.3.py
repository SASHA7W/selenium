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


BUTTON = ("xpath", "//input[contains(@id, 'timerButton')]")
BUTTON_TIMER = wait.until(EC.element_to_be_clickable(BUTTON))
BUTTON_TIMER.click()
print("Button is clickable now")

alert = wait.until(EC.alert_is_present())
print("alert is present now")
driver.switch_to.alert
print(alert.text)
alert.accept()
print("alert was closed")

