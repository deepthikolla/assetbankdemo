from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

@step('I am on my Assetbank login page')
def step_impl(context):
    context.login_page.navigate("https://testclub.assetbank-server.com/")
    assert_equal(context.login_page.get_page_title(), "Asset Bank | Login")

@step('I enter a valid email for my server')
def step_impl(context):
    context.login_page.enter_username("deepthi@testclub.io")

@step('I enter associated valid password')
def step_impl(context):
    context.login_page.enter_password("June@2018")    

@step('I opt to Login')
def step_impl(context):
    context.login_page.submit()

@step('I am directed to my Assetbank dashboard')
def step_impl(context):
    assert_equal(context.dashboard_page.find_header(), "Welcome to Asset Bank")
