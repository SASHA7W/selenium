from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)