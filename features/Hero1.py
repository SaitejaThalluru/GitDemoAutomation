from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service(r"C:\Users\ThalluruSaiteja\Downloads\chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.maximize_window()
driver.get("http://202.56.238.216/#/")
# Verify Logo, Mobile number, Email

print(driver.find_element(By.XPATH, "//div[@class='p-2 font-semibold']").text)
assert "support@heroibl.com" in driver.find_element(By.XPATH, "//div[@class='p-2 font-semibold']").text
print(driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]").text)



# Verify Chat Assistant icon


