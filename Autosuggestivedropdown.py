import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service(r"C:\Users\ThalluruSaiteja\Downloads\chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("am")
time.sleep(3)
countries = driver.find_elements(By.CLASS_NAME, "ui-menu-item")
print(len(countries))
for country in countries:
    if country.text == "Bahamas":
        country.click()
        break

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "Bahamas"
