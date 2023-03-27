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

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH, "//a[contains(.,'Shop')]").click()
phones = driver.find_elements(By.CSS_SELECTOR, "app-card")

for phone in phones:
    phone.find_element(By.XPATH, "//i").click()

checkout = driver.find_element(By.XPATH, "//a[contains(.,'Checkout ( 4 )')]")
print(checkout)
checkout.click()
driver.find_element(By.XPATH, "//button[contains(text(),'Checkout')]").click()


driver.find_element(By.XPATH, "//input[@class='validate filter-input form-control ng-untouched ng-pristine ng-valid']").send_keys('Ind')
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[.='India']")))

driver.find_element(By.XPATH, "//a[.='India']").click()
driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
driver.find_element(By.XPATH, "//input[contains(@value,'Purchase')]").click()
success = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(success)
assert "Success! Thank you! Your order will be delivered in next few weeks :-)" in success



