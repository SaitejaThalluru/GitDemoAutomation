from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service(r"C:\Users\ThalluruSaiteja\Downloads\chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.maximize_window()
driver.get("http://202.56.238.216/#/")
print(driver.current_url)
print(driver.title)
driver.get("http://test.blaze.solar/")
print(driver.title)
print(driver.current_url)
driver.back()
driver.refresh()
driver.forward()
driver.close()
