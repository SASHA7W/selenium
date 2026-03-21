from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)

driver.get("https://demoqa.com/selectable")
GRID = ("xpath", '//button[@id="demo-tab-grid"]')
driver.find_element(*GRID).click()

ONE = ("xpath", "//li[contains(@class, 'list-group-item') and  contains(text(), 'One' )]")
TWO = ("xpath", "//li[contains(text(), 'Two' )]")
THREE = ("xpath", "//li[contains(text(), 'Three' )]")

driver.find_element(*ONE).click()
driver.find_element(*TWO).click()
driver.find_element(*THREE).click()

locators = [ONE, TWO, THREE]
for loc in locators:
    value = driver.find_element(*loc).get_attribute('class')
    print("After check active: ",value)

assert "active" in driver.find_element(*ONE).get_attribute('class'), "First element is not active"
assert "active" in driver.find_element(*TWO).get_attribute('class'), "Second element is not active"
assert "active" in driver.find_element(*THREE).get_attribute('class'), "Third element is not active"

driver.find_element(*ONE).click()
driver.find_element(*TWO).click()
driver.find_element(*THREE).click()

for loc in locators:
    value = driver.find_element(*loc).get_attribute('class')
    print("After check inactive: ", value)

classes = driver.find_element(*ONE).get_attribute("class").split()
assert "active" not in classes, "Element should not have active class"
classes = driver.find_element(*TWO).get_attribute("class").split()
assert "active" not in classes, "Element should not have active class"
classes = driver.find_element(*THREE).get_attribute("class").split()
assert "active" not in classes, "Element should not have active class"

print(driver.find_element(*ONE).is_selected())
print(driver.find_element(*TWO).is_selected())
print(driver.find_element(*THREE).is_selected())

#assert "active" not in driver.find_element(*ONE).get_attribute('class'), "First element is active"
#assert "active" not in driver.find_element(*TWO).get_attribute('class'), "Second element is active"
#assert "active" not in driver.find_element(*THREE).get_attribute('class'), "Third element is active"
#WebDriverWait(driver, 10).until(
   # lambda d: "active" in d.find_element(*ONE_CHECK).get_attribute('class')
   #locators = {"Первый": ONE, "Второй": TWO, "Третий": THREE}

#for name, loc in locators.items():
    # 1. Считаем результат (True/False)
    #is_active = "active" in driver.find_element(*loc).get_attribute("class")
    
    # 2. Выводим в консоль
   # print(f"{name} чекбокс активен: {is_active}")
    
    # 3. Проверяем в тесте
   # assert is_active, f"Ошибка: {name} элемент не стал активным!"