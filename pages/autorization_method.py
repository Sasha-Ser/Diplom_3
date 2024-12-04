import allure
from pages.base_page import BasePage
from locators.locators_login_page import LocatorsLoginPage
from locators.locators_main_page import LocatorsMainPage
from data import Data

class AutorizationMethod(BasePage):

    @allure.step('Авторизация созданным пользователя')
    def  autorization_by_user(self):
        self.click_to_element(LocatorsMainPage.PERSONAL_CABINET_BUTTON)
        self.add_text_to_element(LocatorsLoginPage.LOGIN_EMAIL_FIELD, Data.TEST_USER["email"])
        self.add_text_to_element(LocatorsLoginPage.LOGIN_PASSWORD_FIELD, Data.TEST_USER["password"])
        self.click_to_element(LocatorsLoginPage.LOGIN_BUTTON)
