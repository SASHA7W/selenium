from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://pogoda.interia.pl/prognoza-dlugoterminowa-wroclaw,cId,39240")
time.sleep(3)
driver.find_element(By.XPATH, "//a[contains(text(), 'Polska')]").click()

time.sleep(10)