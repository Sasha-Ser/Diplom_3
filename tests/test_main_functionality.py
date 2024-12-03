import requests
import pytest
import allure


from data import Data
from locators.locators_main_page import LocatorsMainPage
from locators.locators_login_page import LocatorsLoginPage
from locators.locators_personal_cabinet_page import LocatorsPersonalCabinet
from pages.main_page import MainPage
from pages.general_methods import GeneralMethods

class TestMainFunctionality:

    @allure.title('Проверка перехода в конструктор')
    def test_go_to_constructor_success(self, setup_driver):
        driver = MainPage(setup_driver)
        driver.click_to_element(LocatorsMainPage.PERSONAL_CABINET_BUTTON)
        driver.click_to_element(LocatorsMainPage.CONSTRUCTOR_BUTTON)
        driver.find_element_with_wait(LocatorsMainPage.PERSONAL_CABINET_BUTTON)
        assert driver.get_link() == Data.SITE_URL

    @allure.title('Проверка перехода в ленту заказов')
    def test_go_to_order_feed_success(self, setup_driver):
        driver = MainPage(setup_driver)
        driver.click_to_element(LocatorsMainPage.ORDER_FEED_BUTTON)
        assert driver.get_link() == f"{Data.SITE_URL}{Data.ORDER_FEED_PAGE}"

    @allure.title('Проверка появления всплывающего окна после клика по ингредиенту')
    def test_window_with_add_info_about_ingredient_success(self, setup_driver):
        driver = MainPage(setup_driver)
        driver.click_to_element(LocatorsMainPage.BUN_FOR_BURGER)
        assert driver.find_element_with_wait(LocatorsMainPage.TITLE_ADD_INFO_WINDOW).text == "Детали ингредиента"

    @allure.title('Проверка закрытия окна с доп информацией об ингредиенте')
    def test_close_window_with_add_info_success(self, setup_driver):
        driver = MainPage(setup_driver)
        driver.click_to_element(LocatorsMainPage.BUN_FOR_BURGER)
        driver.click_to_element(LocatorsMainPage.ADD_INFO_CLOSE_BUTTON)
        assert driver.wait_for_disappear(LocatorsMainPage.ADD_INFO_CLOSE_BUTTON)

    @allure.title('Проверка увеличения счетчика кол-ва ингредиента')
    def test_increase_ingredient_counter_success(self, setup_driver):
        driver = MainPage(setup_driver)
        driver.drag_and_drop(LocatorsMainPage.BUN_FOR_BURGER, LocatorsMainPage.CONSTRUCTOR_BURGER)
        assert driver.find_element_with_wait(LocatorsMainPage.COUNTER_FOR_BUN).text == '2'

    @allure.title('Проверка создания заказа авторизованным пользователем')
    def test_close_window_with_add_info_success(self, setup_driver):
        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", json=Data.TEST_USER)
        driver = GeneralMethods(setup_driver)
        driver.autorization_by_user()
        driver = MainPage(setup_driver)
        driver.find_element_with_wait(LocatorsMainPage.BUN_FOR_BURGER)
        driver.drag_and_drop(LocatorsMainPage.BUN_FOR_BURGER, LocatorsMainPage.CONSTRUCTOR_BURGER)
        driver.click_to_element(LocatorsMainPage.CREATE_ORDER_BUTTON)
        assert driver.wait_for_change_text(LocatorsMainPage.ID_ORDER, "9999")
        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/login", json=Data.TEST_USER)
        r = response.json()
        access_token = r["accessToken"]
        headers = {'Authorization': f'{access_token}'}
        response = requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)
