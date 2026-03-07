from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get ("https://the-internet.herokuapp.com/status_codes")
count = len(driver.find_elements(By.CSS_SELECTOR, "li a"))
print(count)
for element in range(count):
    status = driver.find_element("xpath", f"//li[{element+1}]/a")
    status.click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
