from pages.BaseApp import BasePage
from locators.locator_form import PageLocators as Locators
from selenium.webdriver.common.keys import Keys
import time


class FormPage(BasePage):

    def find_bth_login(self):
        '''Функция кликает по кнопке войти'''
        self.find_element(Locators.LOCATOR_LOGIN_IN).click()

    def enter_email(self, email: str):
        '''Функция вводит login в поле email'''
        self.find_element(Locators.LOCATOR_INPUT_EMAIL).send_keys(email)

    def enter_password(self, password: str):
        '''Функция вводит password в поле password'''
        self.find_element(Locators.LOCATOR_INPUT_PASSWORD).send_keys(password)
        time.sleep(35)

    def login_in(self):
        '''Функция вводит нажимает войти'''
        self.find_element(Locators.LOCATOR_SUBMIT).click()

    def find_ip(self):
        ip1 = self.find_element(Locators.LOCATOR_IP_ONE).text
        ip2 = self.find_element(Locators.LOCATOR_IP_TWO).text
        t1 = self.find_element(Locators.LOCATOR_TIME_ONE).get_attribute("innerHTML")
        t2 = self.find_element(Locators.LOCATOR_TIME_TWO).get_attribute("innerHTML")
        t1 = t1[t1.find("25"):].strip()
        t2 = t2[t2.find("25"):].strip()
        print(f'{ip1} - {t1}\n{ip2} - {t2}')
