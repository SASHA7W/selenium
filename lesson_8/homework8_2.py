from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/status_codes")

status200 = driver.find_element("xpath", "//a[contains(./@href, 'status_codes/200')]")
status200.click()
time.sleep(5)
home = driver.find_element("xpath", "//a[contains(./@href, 'here')]")
time.sleep(5)

status300 = driver.find_element("xpath", "//a[contains(./@href, 'status_codes/300')]")
status300.click()
time.sleep(5)
home = driver.find_element("xpath", "//a[contains(./@href, 'here')]")
time.sleep(5)

status400 = driver.find_element("xpath", "//a[contains(./@href, 'status_codes/400')]")
status400.click()
time.sleep(5)
home = driver.find_element("xpath", "//a[contains(./@href, 'here')]")
time.sleep(5)

status500 = driver.find_element("xpath", "//a[contains(./@href, 'status_codes/500')]")
status500.click()
time.sleep(5)
home = driver.find_element("xpath", "//a[contains(./@href, 'here')]")
time.sleep(5)