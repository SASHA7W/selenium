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

# 1. Сначала даем паузу ПОСЛЕ капчи, чтобы DOM "ожил"
time.sleep(3) 

def click_js(element):
    driver.execute_script("arguments[0].click();", element)

# Клик по городу (делаем необязательным через try-except)
try:
    # Используем CSS-селектор, он часто стабильнее на Авито
    loc_btn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-marker='location/tooltip-leave-as-is']"))
    )
    click_js(loc_btn)
    print("Город подтвержден")
except:
    print("Кнопка города не найдена или уже исчезла")

# Клик по категориям (основная цель)
try:
    # Ждем именно присутствия в DOM, а потом кликаем через JS
    cat_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(("xpath", "//span[contains(text(), 'Все категории')]"))
    )
    # Скроллим к кнопке на всякий случай
    driver.execute_script("arguments[0].scrollIntoView(true);", cat_btn)
    time.sleep(1)
    click_js(cat_btn)
    print("Меню категорий открыто!")
except Exception as e:
    print(f"Не удалось нажать на категории: {e}")
