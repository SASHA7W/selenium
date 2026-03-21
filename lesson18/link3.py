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

driver.get("https://www.ozon.ru/")
LINK_3PAGE = ("xpath", "//div[contains(text(), 'Каталог')]")

try:
    katalog = wait.until(EC.presence_of_element_located(LINK_3PAGE))
    katalog.click()
    print("The catalog is opened")
except:
    print("the button catalog not found")
    time.sleep(3)