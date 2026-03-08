from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")

driver.current_url
driver.title
driver.page_source

PAGE_URL = driver.current_url
print("Current URL", PAGE_URL)
PAGE_TITLE = driver.title 
print ("Title page", PAGE_TITLE)
PAGE_SOURCE = driver.page_source
print(PAGE_SOURCE)
current_title = driver.title
driver.get("https://dzen.ru")
assert current_title == "Дзен", "Страница не открылась"
