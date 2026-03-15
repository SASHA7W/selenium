import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demowebshop.tricentis.com/books")


ELEMENTS = driver.find_elements(By.CLASS_NAME, "btn-wrap") # Находим все элементы h2
print(ELEMENTS[10])

