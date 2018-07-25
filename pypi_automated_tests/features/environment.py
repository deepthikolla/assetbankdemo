from selenium import webdriver
from browser import Browser
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.dashboard_page = DashboardPage()

def after_all(context):
    context.browser.close()