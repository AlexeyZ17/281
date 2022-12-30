# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from settings import valid_phone, valid_email, valid_password
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import pytest


"""настройки работы веб-драйвера"""
driver = webdriver.Chrome()
driver.implicitly_wait(5)


# python -m pytest -v --driver Chrome --driver-path C:\Windows\chromedriver.exe tests.py


# @pytest.fixture(autouse=True)
# def testing():
#     selenium = webdriver.Chrome()
#     # Переходим на страницу авторизации
#     selenium.get('https://b2c.passport.rt.ru/')
#
#     # Для визуального контроля
#     time.sleep(3)
#
#     yield selenium
#     selenium.quit()


'''дымовое тестирование страницы авторизации'''
# def test_open_auth_page(selenium):
#     selenium.get('https://b2c.passport.rt.ru/')
#     time.sleep(5)
#     assert selenium.find_element(By.CLASS_NAME, 'card-container__title').text == "Авторизация"
#
#     assert selenium.find_element(By.ID, 't-btn-tab-phone').text == "Телефон"
#     selenium.quit()


'''Позитивное тестирование:'''
'''тестирование страницы авторизации вход по валидному телефону и паролю'''
# def test_auth_page_valid_phone(selenium):
#     selenium.get('https://b2c.passport.rt.ru/')
#     time.sleep(5)
#     selenium.find_element(By.ID, 'username').send_keys(valid_phone)
#     selenium.find_element(By.ID, 'password').send_keys(valid_password)
#     selenium.find_element(By.ID,'kc-login').click()
#     time.sleep(5)
#     assert selenium.find_element(By.ID, 'logout-btn').text == "Выйти"
#
#     selenium.quit()


'''тестирование страницы авторизации вход по валидной почте и паролю'''
# def test_auth_page_valid_mail(selenium):
#     selenium.get('https://b2c.passport.rt.ru/')
#     time.sleep(5)
#     selenium.find_element(By.ID, 't-btn-tab-mail').click()
#     selenium.find_element(By.ID, 'username').send_keys(valid_email)
#     selenium.find_element(By.ID, 'password').send_keys(valid_password)
#     selenium.find_element(By.ID,'kc-login').click()
#     time.sleep(5)
#     assert selenium.find_element(By.ID, 'logout-btn').text == "Выйти"
#
#     selenium.quit()



'''тестирование страницы авторизации: автоматическое переключение таб на вход по валидной почте и паролю'''
# def test_auth_page_valid_mail(selenium):
#     selenium.get('https://b2c.passport.rt.ru/')
#     time.sleep(5)
#     selenium.find_element(By.ID, 'username').send_keys(valid_email)
#     selenium.find_element(By.ID, 'password').click()
#     selenium.find_element(By.ID, 'password').send_keys(valid_password)
#     selenium.find_element(By.ID, 'kc-login').click()
#     time.sleep(5)
#     assert selenium.find_element(By.ID, 'logout-btn').text == "Выйти"
#
#     selenium.quit()


'''тестирование страницы авторизации: проверка работоспособности кнопки "забыли пароль"'''
# def test_auth_page_btn(selenium):
#     selenium.get('https://b2c.passport.rt.ru/')
#     time.sleep(5)
#     selenium.find_element(By.ID, 'forgot_password').click()
#     time.sleep(5)
#     assert selenium.find_element(By.CLASS_NAME, 'card-container__title').text == "Восстановление пароля"
#
#     selenium.quit()


'''тестирование страницы авторизации: проверка работоспособности кнопки "Зарегистрироваться"'''
# def test_auth_page_btn(selenium):
#     selenium.get('https://b2c.passport.rt.ru/')
#     time.sleep(5)
#     selenium.find_element(By.ID, 'kc-register').click()
#     assert selenium.find_element(By.CLASS_NAME, 'card-container__title').text == "Регистрация"
#
#     selenium.quit()


'''тестирование страницы авторизации: проверка работоспособности кнопки "пользовательское соглашение"'''
# def test_auth_page_btn(selenium):
#     selenium.get('https://b2c.passport.rt.ru/')
#     time.sleep(5)
#     selenium.find_element(By.CLASS_NAME, "auth-policy").click()
#     assert selenium.find_element(By.CLASS_NAME, 'offer-title').text == "Публичная оферта о заключении Пользовательского соглашения на использование Сервиса «Ростелеком ID»"
#
#     selenium.quit()



'''НЕГАТИВНОЕ ТЕСТИРОВАНИЕ:'''
'''тестирование страницы авторизации вход по НЕ валидному телефону и валидному паролю'''
# def test_auth_page_NOvalid_telephon(selenium):
#     selenium.get('https://b2c.passport.rt.ru/')
#     time.sleep(5)
#     selenium.find_element(By.ID, 'username').send_keys("+79258479832")
#     selenium.find_element(By.ID, 'password').send_keys(valid_password)
#     selenium.find_element(By.ID,'kc-login').click()
#     time.sleep(5)
#     assert selenium.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"
#
#     selenium.quit()

'''тестирование страницы авторизации вход по НЕ валидному паролю и валидному телефону'''
# def test_auth_page_NOvalid_password(selenium):
#     selenium.get('https://b2c.passport.rt.ru/')
#     time.sleep(5)
#     selenium.find_element(By.ID, 'username').send_keys(valid_phone)
#     selenium.find_element(By.ID, 'password').send_keys("Lav654322")
#     selenium.find_element(By.ID,'kc-login').click()
#     time.sleep(5)
#     assert selenium.find_element(By.ID, 'form-error-message').text == "Неверно введен текст с картинки"
#
#     selenium.quit()


'''тестирование страницы авторизации вход по НЕ валидной почте и валидному паролю'''
# def test_auth_page_valid_mail(selenium):
#     selenium.get('https://b2c.passport.rt.ru/')
#     time.sleep(5)
#     selenium.find_element(By.ID, 't-btn-tab-mail').click()
#     selenium.find_element(By.ID, 'username').send_keys("luckin.alexej@yande.ru")
#     selenium.find_element(By.ID, 'password').send_keys("Lav654321")
#     selenium.find_element(By.ID,'kc-login').click()
#     time.sleep(5)
#     assert selenium.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"
#
#     selenium.quit()

'''тестирование страницы авторизации вход по НЕ валидному паролю и валидной почте '''
# def test_auth_page_valid_mail(selenium):
#     selenium.get('https://b2c.passport.rt.ru/')
#     time.sleep(5)
#     selenium.find_element(By.ID, 't-btn-tab-mail').click()
#     selenium.find_element(By.ID, 'username').send_keys(valid_email)
#     selenium.find_element(By.ID, 'password').send_keys("Lav654311")
#     selenium.find_element(By.ID,'kc-login').click()
#     time.sleep(5)
#     assert selenium.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"
#
#     selenium.quit()




'''Черновик'''
# assert driver.find_element(By.ID, 't-btn-tab-phone').text == "Телефон"
#         elements = driver.find_elements(BY.CLASS_NAME, "tabs-input-container")
# assert "Телефон" and "Почта" in elements
#
# elements = driver.find_elements(By.CLASS_NAME, "rt-tabs rt-tabs--orange rt-tabs--small tabs-input-container__tabs")
# assert "Телефон" and "Почта" in elements