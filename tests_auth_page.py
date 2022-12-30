from settings import valid_phone, valid_password
from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

"""настройки работы веб-драйвера"""
driver = webdriver.Chrome()
driver.implicitly_wait(5)


# python -m pytest -v --driver Chrome --driver-path C:\Windows\chromedriver.exe tests_auth_page.py


class AuthLocators:
    LOCATOR_AUTH_PHONE_TAB = (By.ID, "t-btn-tab-phone")
    LOCATOR_AUTH_EMAIL_TAB = (By.ID, "t-btn-tab-mail")
    LOCATOR_AUTH_LOGIN_TAB = (By.ID, "t-btn-tab-login")
    LOCATOR_AUTH_LS_TAB = (By.ID, "t-btn-tab-ls")
    LOCATOR_AUTH_PASS_BTN = (By.ID, "password")
    LOCATOR_AUTH_BAR = (By.CLASS_NAME, "tabs-input-container")

class AuthPage(BasePage):
   def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        driver.get("https://b2c.passport.rt.ru/")
        self.username = driver.find_element(By.ID, "username")
        self.password = driver.find_element(By.ID, "password")
        self.btn = driver.find_element(By.ID, "kc-login")


    def authorization_by_phone(self):
        self.find_element(AuthLocators.LOCATOR_AUTH_PHONE_TAB, time=5).click()


    def authorization_by_email(self):
        self.find_element(AuthLocators.LOCATOR_AUTH_EMAIL_TAB, time=5).click()


    def authorization_by_login(self):
        self.find_element(AuthLocators.LOCATOR_AUTH_LOGIN_TAB, time=5).click()


    def authorization_by_ls(self):
        self.find_element(AuthLocators.LOCATOR_AUTH_LS_TAB, time=5).click()

    def enter_username(self):
        self.username.send_keys(valid_phone)

    def enter_password(self):
        self.password.send_keys(valid_password)


    def btn_click(self):
        self.btn.click()
