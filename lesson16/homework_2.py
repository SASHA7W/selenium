import time
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
wait = WebDriverWait(driver, 10, poll_frequency=1) 

driver.get("https://demoqa.com/select-menu")
input_multiselect = driver.find_element("xpath", "//input[@id='react-select-4-input']")]
input_multiselect.send_keys("Bla")
assert input_multiselect.get_attribute('value') == 'Bla', "The text don't input"
input_multiselect.send_keys(Keys.TAB)
time.sleep(3)
