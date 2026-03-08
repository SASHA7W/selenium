import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://pogoda.interia.pl/prognoza-szczegolowa-wroclaw,cId,39240")
time.sleep(10)
driver.forward()
time.sleep(7)
driver.back()
time.sleep(9)
driver.forward()
time.sleep(5)
driver.refresh()
time.sleep(10)
