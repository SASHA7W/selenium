from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")
fullName = driver.find_element("xpath", "//input[@id='userName']")
email = driver.find_element("xpath", "//input[@id='userEmail']")
currentAddress = driver.find_element("xpath", "//textarea[@id='currentAddress']")
permanentAddress = driver.find_element("xpath", "//textarea[@id='permanentAddress']")
submitButton = driver.find_element("xpath", "//button[@id='submit']")

assert (fullName.get_property("value") or "") == ""
fullName.send_keys("John Ferry")
assert "John Ferry" in fullName.get_property("value")
fullName_value = fullName.get_property("value")
assert fullName_value == "John Ferry", f"Ожидалось 'John Ferry', но в поле: '{fullName_value}'"

assert (email.get_attribute("value") or "") == ""
email.send_keys("john.ferry@google.com")
assert "john.ferry@google.com" in email.get_attribute("value")
email_value = email.get_attribute("value")
assert "john.ferry@google.com" in email_value

assert (currentAddress.get_attribute("value") or "") == ""
currentAddress.send_keys("Kiev, Ukraine, st. Bohdana Chmelnytskogo, 15")
assert "Kiev, Ukraine, st. Bohdana Chmelnytskogo, 15" in currentAddress.get_attribute("value")
currentAddress_value = currentAddress.get_attribute("value")
assert "Kiev, Ukraine, st. Bohdana Chmelnytskogo, 15" in currentAddress_value


assert (permanentAddress.get_attribute("value") or "") == ""
permanentAddress.send_keys("This is permanent address")
assert "This is permanent address" in permanentAddress.get_attribute("value")
permanentAddress_value = permanentAddress.get_attribute("value")
assert "This is permanent address" in permanentAddress_value

time.sleep(5)
