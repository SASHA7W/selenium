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

driver.get("https://hyperskill.org/login")
try:
    alert = wait.until(EC.alert_is_present())
    print(f"Alert found: {alert.text}")
    alert.accept
except:
    print("No alert present, continuing to login...")
try:
    google_xpath = "xpath", "//button[@click-event-target='jetbrains_account']"
    link_1page = wait.until(EC.element_to_be_clickable(google_xpath))
    link_1page.click()
    print('Jet brains account button clicked successfully!')
except:
     # 4. If regular click fails, FORCE it with JavaScript
    driver.execute_script("arguments[0].click();", link_1page)
    print("Click forced via JavaScript!")

