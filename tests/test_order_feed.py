import requests
import pytest
import allure
from selenium import webdriver


from data import Data
from locators.locators_main_page import LocatorsMainPage
from locators.locators_order_feed import LocatorsOrderFeedPage
from locators.locators_pass_recovery_page import LocatorsPassRecovery
from locators.locators_login_page import LocatorsLoginPage
from locators.locators_personal_cabinet_page import LocatorsPersonalCabinet
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.general_methods import GeneralMethods

class TestOrderFeed:

    # Создание тестового пользователя
    @classmethod
    def setup_class(cls):
        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", json=Data.TEST_USER)


    @allure.title('Проверка открытия модального окна с заказом из "Истории заказов" в лк')
    def test_pen_modal_window_with_order_info(self, setup_driver):
        driver = GeneralMethods(setup_driver)
        driver.autorization_by_user()
        driver.creation_order()
        driver = MainPage(setup_driver)
        driver.click_to_element(LocatorsMainPage.PERSONAL_CABINET_BUTTON)
        driver.click_to_element(LocatorsPersonalCabinet.ORDER_HISTORY_BUTTON)
        driver.find_element_with_wait(LocatorsPersonalCabinet.ORDER_INFO)
        driver.click_to_element(LocatorsPersonalCabinet.ORDER_INFO)
        assert driver.find_element_with_wait(LocatorsPersonalCabinet.MODAL_WINDOW_WITH_ORDER)

    @allure.title('Проверка появления заказа в ленте заказов')
    def test_appearance_order_in_order_feed(self, setup_driver):
        driver = GeneralMethods(setup_driver)
        driver.autorization_by_user()
        id_order = driver.creation_order()
        driver = MainPage(setup_driver)
        driver.click_to_element(LocatorsMainPage.ORDER_FEED_BUTTON)
        driver = OrderFeedPage(setup_driver)
        assert driver.find_element_among_set_with_wait(LocatorsOrderFeedPage.LIST_OF_ORDER, f"0{id_order}")

    @allure.title('Проверка появления заказа в ленте заказов в статусе "В работе"')
    def test_appearance_order_in_progress(self, setup_driver):
        driver = GeneralMethods(setup_driver)
        driver.autorization_by_user()
        id_order = driver.creation_order()
        driver = MainPage(setup_driver)
        driver.click_to_element(LocatorsMainPage.ORDER_FEED_BUTTON)
        driver.wait_for_change_text(LocatorsOrderFeedPage.ORDER_IN_PROGRESS, "Все текущие заказы готовы!")
        assert id_order in driver.find_element_with_wait(LocatorsOrderFeedPage.ORDER_IN_PROGRESS).text

    @allure.title('Проверка увеличения счетчика заказов за все время на странице Лента заказов')
    def test_increase_counter_order_all_time(self, setup_driver):
        driver = MainPage(setup_driver)
        driver.click_to_element(LocatorsMainPage.ORDER_FEED_BUTTON)
        old_counter_order_all_time = driver.find_element_with_wait(LocatorsOrderFeedPage.COUNTER_ORDERS_ALL_TIME).text
        driver = GeneralMethods(setup_driver)
        driver.autorization_by_user()
        driver.creation_order()
        driver = MainPage(setup_driver)
        driver.click_to_element(LocatorsMainPage.ORDER_FEED_BUTTON)
        assert int(old_counter_order_all_time) < int(driver.find_element_with_wait(LocatorsOrderFeedPage.
                                                                                   COUNTER_ORDERS_ALL_TIME).text)

    @allure.title('Проверка увеличения счетчика заказов за сегодня на странице Лента заказов')
    def test_increase_counter_order_today(self, setup_driver):
        driver = MainPage(setup_driver)
        driver.click_to_element(LocatorsMainPage.ORDER_FEED_BUTTON)
        old_counter_order_today = driver.find_element_with_wait(LocatorsOrderFeedPage.COUNTER_ORDERS_TODAY).text
        driver = GeneralMethods(setup_driver)
        driver.autorization_by_user()
        driver.creation_order()
        driver = MainPage(setup_driver)
        driver.click_to_element(LocatorsMainPage.ORDER_FEED_BUTTON)
        assert int(old_counter_order_today) < int(
            driver.find_element_with_wait(LocatorsOrderFeedPage.COUNTER_ORDERS_TODAY).text)

    # Удаление тестового пользователя
    @classmethod
    def teardown_class(cls):
        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/login", json=Data.TEST_USER)
        r = response.json()
        access_token = r["accessToken"]
        headers = {'Authorization': f'{access_token}'}
        response = requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)
