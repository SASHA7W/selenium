import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
# Убирает надпись "Браузером управляет автоматизированное ПО"
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# Основной флаг, скрывающий факт автоматизации
options.add_argument("--disable-blink-features=AutomationControlled")

options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")
options.page_load_strategy = 'normal'

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1) 

#driver.get("https://google.com")
first_tab = driver.current_window_handle
print(first_tab)
driver.switch_to.new_window("tab")
second_tab = driver.current_window_handle
driver.switch_to.new_window("tab")
print(second_tab)
third_tab = driver.current_window_handle
print(third_tab)
list_of_tabs = driver.window_handles
print(list_of_tabs)
time.sleep(5)

driver.switch_to.window(list_of_tabs[0])
time.sleep(5)
driver.get("https://hyperskill.org/login")
PAGE1_TITLE = driver.title

driver.switch_to.window(list_of_tabs[1])
driver.get("https://www.avito.ru/")
PAGE2_TITLE = driver.title

driver.switch_to.window(list_of_tabs[2])
driver.get("https://www.ozon.ru/")
PAGE3_TITLE = driver.title
print("Title 1: ", PAGE1_TITLE, "Title 2:", PAGE2_TITLE, "Title 3: ",PAGE3_TITLE)

driver.switch_to.window(list_of_tabs[0])
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
    print('Jet Brains account button clicked successfully!')
except:
     # 4. If regular click fails, FORCE it with JavaScript
    driver.execute_script("arguments[0].click();", link_1page)
    print("Click forced via JavaScript!")

driver.switch_to.window(list_of_tabs[1])

loc_leave = ("xpath", "//button[@data-marker='location/tooltip-leave-as-is']")
all_categories = ("xpath", "//button[@data-marker='top-rubricator/all-categories']")

try:
    confirm_city = wait.until(EC.element_to_be_clickable(loc_leave))
    driver.execute_script("arguments[0].click();", confirm_city)
    print("city confirmed")
except: 
    print("City tooltip not found, skipping...")

try:
    all_categories = wait.until(EC.presence_of_element_located(all_categories))
    driver.execute_script("arguments[0].click();", all_categories)
    print("Categories menu opened")
except:
    print("Failed to open categories:")

driver.switch_to.window(list_of_tabs[2])
LINK_3PAGE = ("xpath", "//div[contains(text(), 'Каталог')]")

try:
    katalog = wait.until(EC.presence_of_element_located(LINK_3PAGE))
    katalog.click()
    print("The catalog is opened")
except:
    print("the button catalog not found")