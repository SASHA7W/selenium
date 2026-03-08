from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.diki.pl/slownik-angielskiego?q=something")
time.sleep(3)

current_title = driver.title
print("Title diki.pl", current_title)

driver.get("https://ya.ru/")
current_title2 = driver.title
print("Title ya.ru", current_title2)

driver.refresh()

current_page=driver.current_url
print("Current Url", current_page)

driver.back()
url=driver.current_url
assert url == "https://ya.ru/", "This is previous page"

