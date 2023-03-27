from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service(r"C:\Users\ThalluruSaiteja\Downloads\chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option1":
        checkbox.click()
        assert checkbox.is_selected()
        break


Radiobuttons = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
print(len(Radiobuttons))
for radiobutton in Radiobuttons:
    if radiobutton.get_attribute("value") == "radio1":
        radiobutton.click()
        assert radiobutton.is_selected()
        break


assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "show-textbox").click()
assert driver.find_element(By.ID, "displayed-text").is_displayed()
