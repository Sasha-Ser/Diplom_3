import requests
import pytest
import allure
from selenium import webdriver


from data import Data
from locators.locators_main_page import LocatorsMainPage
from locators.locators_pass_recovery_page import LocatorsPassRecovery
from locators.locators_login_page import LocatorsLoginPage
from locators.locators_personal_cabinet_page import LocatorsPersonalCabinet
from pages.main_page import MainPage
from pages.general_methods import GeneralMethods

class TestPersonalCabinet:

    # Создание тестового пользователя
    @classmethod
    def setup_class(cls):
        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", json=Data.TEST_USER)


    @allure.title('Проверка перехода в личный кабинет')
    def test_go_to_personal_cabinet_success(self, setup_driver):
        driver = GeneralMethods(setup_driver)
        driver.autorization_by_user()
        driver = MainPage(setup_driver)
        driver.click_to_element(LocatorsMainPage.PERSONAL_CABINET_BUTTON)
        driver.find_element_with_wait(LocatorsPersonalCabinet.ORDER_HISTORY_BUTTON)
        assert driver.get_link() == f'{Data.SITE_URL}{Data.PERSONAL_CABINET_PAGE}'

    @allure.title('Проверка перехода к истории заказов')
    def test_go_to_order_history_success(self, setup_driver):
        driver = GeneralMethods(setup_driver)
        driver.autorization_by_user()
        driver = MainPage(setup_driver)
        driver.click_to_element(LocatorsMainPage.PERSONAL_CABINET_BUTTON)
        driver.click_to_element(LocatorsPersonalCabinet.ORDER_HISTORY_BUTTON)
        assert driver.get_link() == f'{Data.SITE_URL}{Data.ORDER_HISTORY_PAGE}'

    @allure.title('Проверка выхода из аккаунта')
    def test_exit_from_personal_cabinet_success(self, setup_driver):
        driver = GeneralMethods(setup_driver)
        driver.autorization_by_user()
        driver = MainPage(setup_driver)
        driver.click_to_element(LocatorsMainPage.PERSONAL_CABINET_BUTTON)
        driver.click_to_element(LocatorsPersonalCabinet.EXIT_BUTTON)
        driver.find_element_with_wait(LocatorsLoginPage.PASS_RECOVER_LINK)
        assert driver.get_link() == f'{Data.SITE_URL}{Data.LOGIN_PAGE}'

    # Удаление тестового пользователя
    @classmethod
    def teardown_class(cls):
        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/login", json=Data.TEST_USER)
        r = response.json()
        access_token = r["accessToken"]
        headers = {'Authorization': f'{access_token}'}
        response = requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)
