from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service(r"C:\Users\ThalluruSaiteja\Downloads\chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
# Custom XPATH Syntax = //input[@attribute='value']
driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("hi@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys(123456)
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.CLASS_NAME, "btn-success").click()
Message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(Message)
assert "Success"in Message
# Custom CSS Selector Syntax = input[attribute='value'] or #id or .class name
driver.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("Teja")
driver.find_element(By.CSS_SELECTOR, "input[value='option1']").click()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello")
# static dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Male")
Verify = driver.find_element(By.ID, "exampleFormControlSelect1").text
assert "male" in Verify





driver.close()
