import allure
from pages.base_page import BasePage
from pages.main_page import MainPage
from locators.locators_login_page import LocatorsLoginPage
from locators.locators_main_page import LocatorsMainPage
from data import Data

class GeneralMethods(MainPage, BasePage):

    @allure.step('Авторизация созданным пользователя')
    def  autorization_by_user(self):
        self.click_to_element(LocatorsMainPage.PERSONAL_CABINET_BUTTON)
        self.add_text_to_element(LocatorsLoginPage.LOGIN_EMAIL_FIELD, Data.TEST_USER["email"])
        self.add_text_to_element(LocatorsLoginPage.LOGIN_PASSWORD_FIELD, Data.TEST_USER["password"])
        self.click_to_element(LocatorsLoginPage.LOGIN_BUTTON)

    @allure.step('Создание определенного заказа')
    def creation_order(self):
        self.find_element_with_wait(LocatorsMainPage.BUN_FOR_BURGER)
        self.drag_and_drop(LocatorsMainPage.BUN_FOR_BURGER, LocatorsMainPage.CONSTRUCTOR_BURGER)
        self.click_to_element(LocatorsMainPage.CREATE_ORDER_BUTTON)
        self.wait_for_change_text(LocatorsMainPage.ID_ORDER, "9999")
        order_id = self.get_text_from_element(LocatorsMainPage.ID_ORDER)
        self.click_to_element(LocatorsMainPage.CLOSE_INFO_ORDER_BUTTON)
        return order_id