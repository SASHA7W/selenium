import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")
options.page_load_strategy = 'normal'

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10) 

driver.get ("https://www.avito.ru/")

loc_leave = ("xpath", "//button[@data-marker='location/tooltip-leave-as-is']")
all_categories = ("xpath", "//button[@data-marker='top-rubricator/all-categories']")

try:
    confirm_city = wait.until(EC.element_to_be_clickable(loc_leave))
    driver.execute_script("arguments[0].click();", confirm_city)
    print("city confirmed")
except: 
    print("City tooltip not found, skipping...")

try:
    all_categories = wait.until(EC.element_to_be_clickable(all_categories))
    driver.execute_script("arguments[0].click();", all_categories)
    print("Categories menu opened")
except:
    print("Failed to open categories:")

    