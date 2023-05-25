from selenium.webdriver.common.by import By


class PageLocators:
    """В данном классе определены основные локаторы для поиска объектов на странице согласно задания"""

    LOCATOR_LOGIN_IN = (By.CLASS_NAME, "icon-login") # локатор кнопки входа
    LOCATOR_INPUT_EMAIL = (By.XPATH, '//*[@id="form-login"]/div[1]/div/input') # относительный путь к полю email
    LOCATOR_INPUT_PASSWORD = (By.XPATH, '//*[@id="login-password"]') # относительный путь к полю password
    LOCATOR_SUBMIT = (By.XPATH, '//*[@id="form-login"]/div[7]/button') # относительный путь к кнопке войти в popup авторизации
    LOCATOR_CAPTCHA_CLICK = (By.CLASS_NAME, 'recaptcha-checkbox-border')
    LOCATOR_IP_ONE = (By.XPATH, '//*[@id="el-22245282"]/td[3]/ul/li[1]/div[2]/b')
    LOCATOR_IP_TWO = (By.XPATH, '//*[@id="el-22245281"]/td[3]/ul/li[1]/div[2]/b')
    LOCATOR_TIME_ONE = (By.XPATH, '//*[@id="el-22245282"]/td[3]/ul/li[6]/div[2]')
    LOCATOR_TIME_TWO = (By.XPATH, '//*[@id="el-22245281"]/td[3]/ul/li[6]/div[2]')
