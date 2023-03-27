import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

serv_obj = Service(r"C:\Users\ThalluruSaiteja\Downloads\chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(2)
browserSorted = []

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH, "//span[contains(@class,'sort-icon sort-descending')]").click()
veggieWebelements = driver.find_elements(By.XPATH, "//td[position()=1]")
for element in veggieWebelements:
    browserSorted.append(element.text)

originalBrowserSorted = browserSorted.copy()


assert browserSorted.sort() == originalBrowserSorted

