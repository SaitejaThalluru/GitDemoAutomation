from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'launch browser')
def step_impl(context):
   context.driver=webdriver.Chrome(r"C:\Users\ThalluruSaiteja\Downloads\chromedriver_win32\chromedriver.exe")


@when(u'enter URL')
def step_impl(context):
    context.driver.get("http://202.56.238.216/#/")
    context.driver.implicitly_wait(60)


@then(u'page should open')
def step_impl(context):
    status=context.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").is_displayed()
    assert status is True


@then(u'wait for sometime')
def step_impl(context):
    context.driver.implicitly_wait(30)


@then(u'Close the browser')
def step_impl(context):
    context.driver.close()
