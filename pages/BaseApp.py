from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage:
    """Класс определяет базовые методы для работы с WebDriver"""
    def __init__(self, driver, url='https://proxy6.net'):
        self.driver = driver
        self.url = url

    def find_element(self, locator, time=15):
        '''Функция находит элемент на странице по локатору, аргумент time устанавливает время ожидания'''
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Элемент {locator} не найден'
                                                      )

    def find_elements(self, locator, time=15):
        '''Функция находит все элементы по локатору, аргумент time устанавливает время ожидания'''
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Элементы {locator} не найдены'
                                                      )

    def open_site(self):
        '''Функция получает ссылку на страницу для тестов'''
        time.sleep(10)
        return self.driver.get(self.url)
