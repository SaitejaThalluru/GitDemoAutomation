import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service(r"C:\Users\ThalluruSaiteja\Downloads\chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
Email = 'sajid.imam@mantralabsglobal.com'
Password = 'mHe@dmIn#2020'
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://patientapp.manipalhospitals.com/secure/authv2/admin/login")

# invalid login
# without entering any data
driver.find_element(By.CSS_SELECTOR, "button").click()
print(driver.find_element(By.XPATH, "//div[text()=' Email is required. ']").text)
print(driver.find_element(By.XPATH, "//div[text()=' password is required. ']").text)
# Valid Email & Password
driver.find_element(By.ID, "email_id").send_keys(Email)
driver.find_element(By.NAME, "password").send_keys(Password)
driver.find_element(By.CSS_SELECTOR, "button").click()


# Verify Logged in successfully

Logo = driver.find_element(By.CSS_SELECTOR, ".logo-name").text
assert "Manipal" in Logo
Name = driver.find_element(By.XPATH, "//a[contains(text(),'Sajid')]").text
assert "Sajid" in Name
print(Name)

# Logout
time.sleep(5)
driver.find_element(By.XPATH, "//em[text()='settings']").click()

Change = driver.find_element(By.XPATH, "//span[.='Change Password']").text
print(Change)
assert "Change Password" in Change

Logout = driver.find_element(By.XPATH, "//span[contains(text(),'Logout')]").text
print(Logout)

driver.find_element(By.XPATH, "//span[contains(text(),'Logout')]").click()
login = driver.find_element(By.XPATH, "//span[contains(text(),'Login')]").text
assert "Login" in login

