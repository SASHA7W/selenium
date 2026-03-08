from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://hyperskill.org/courses")
time.sleep(3)
#driver.find_element("xpath", "//a[.//text()[contains(., 'Most popular')]]").click()
#driver.find_element("xpath", "//div[contains(@class, 'categories my-8')]//a[contains(@class, 'active-route router-link-exact-active btn rounded-full btn-category') and contains(.,'New courses')]").click()
#driver.find_element("xpath", "//a[@click-event-context='{\"title\":\"new_courses\"}']")
driver.find_element("xpath", "//a[contains(@click-event-context, '\"title\":\"new_courses\"')]").click()
time.sleep(3)