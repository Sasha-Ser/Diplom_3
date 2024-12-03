from selenium.webdriver.common.by import By


class LocatorsLoginPage:

    PASS_RECOVER_LINK = By.XPATH, ".//a[text()='Восстановить пароль']" #Ссылка "Восстановить пароль" на странице авторизации
    LOGIN_EMAIL_FIELD = By.XPATH, ".//input[@type='text']" # Поле для ввода емайл
    LOGIN_PASSWORD_FIELD = By.XPATH, ".//input[@type='password']"  # Поле для ввода пароля
    LOGIN_BUTTON = By.XPATH, ".//button" #Кнопка "Войти" на странице входа