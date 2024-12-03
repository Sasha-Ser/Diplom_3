from selenium.webdriver.common.by import By


class LocatorsPassRecovery:
    EMAIL_FIELD = By.XPATH, ".//input" #Поле "Email" на странице восстановления пароля
    BUTTON_RECOVERY = By.XPATH, ".//button" #Кнопка "Восстановить" на странице  восстановления пароля
    FIELD_FOR_CODE = By.XPATH, ".//input[@name='name']" #Поле для ввода кода из почты
    BUTTON_SAVE = By.XPATH, ".//button[text() ='Сохранить']" #Кнопка для сохранения изменений на странице
                                                                                    # восстановления пароля
    PASSWORD_FIELD = By.XPATH, ".//input[@name = 'Введите новый пароль']" #Поле для ввода пароля на странице
                                                                                    # восстановления пароля
    CHANGE_VIEW = By.XPATH, ".//div[@class = 'input__icon input__icon-action']" #Иконка глаза на поле с паролем