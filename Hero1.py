from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Users\ThalluruSaiteja\Downloads\chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("http://202.56.238.216/#/")
driver.find_element(By.TAG_NAME, "").click()





