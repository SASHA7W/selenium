from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
import pickle

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
options.add_argument("Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.amazon.com/?ref_=nav_signin&claim_type=MobileNumber&new_account=1&")
home_page = ("https://www.amazon.com/?ref_=nav_signin&claim_type=MobileNumber&new_account=1&")
LINK = ("xpath", "//a[contains(@href, 'Mighty-Patch-Hydrocolloid-Absorbing')]")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LINK)).click()
ADD_TO_CART = driver.find_element("xpath", "//input[contains(@value, 'Add to cart')]")
ADD_TO_CART.click()
time.sleep(3)
allCookies = driver.get_cookies()
time.sleep(5)
driver.delete_all_cookies()

driver.get("https://www.amazon.com/?ref_=nav_signin&claim_type=MobileNumber&new_account=1&")

for cookie in allCookies:
    try:
        driver.add_cookie(cookie)
    except Exception as e:
        print(f"Не удалось добавить куки {e}")