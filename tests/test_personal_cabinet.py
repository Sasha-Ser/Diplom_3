import requests
import pytest
import allure
from selenium import webdriver


from data import Data
from locators.locators_main_page import LocatorsMainPage
from locators.locators_login_page import LocatorsLoginPage
from locators.locators_personal_cabinet_page import LocatorsPersonalCabinet
from pages.main_page import MainPage
from pages.autorization_method import AutorizationMethod

class TestPersonalCabinet:

    @allure.title('Проверка перехода в личный кабинет')
    def test_go_to_personal_cabinet_success(self, setup_driver, create_and_delete_user):
        driver = AutorizationMethod(setup_driver)
        driver.autorization_by_user()
        driver = MainPage(setup_driver)
        driver.click_to_element(LocatorsMainPage.PERSONAL_CABINET_BUTTON)
        driver.find_element_with_wait(LocatorsPersonalCabinet.ORDER_HISTORY_BUTTON)
        assert driver.get_link() == f'{Data.SITE_URL}{Data.PERSONAL_CABINET_PAGE}'

    @allure.title('Проверка перехода к истории заказов')
    def test_go_to_order_history_success(self, setup_driver, create_and_delete_user):
        driver = AutorizationMethod(setup_driver)
        driver.autorization_by_user()
        driver = MainPage(setup_driver)
        driver.click_to_element(LocatorsMainPage.PERSONAL_CABINET_BUTTON)
        driver.click_to_element(LocatorsPersonalCabinet.ORDER_HISTORY_BUTTON)
        assert driver.get_link() == f'{Data.SITE_URL}{Data.ORDER_HISTORY_PAGE}'

    @allure.title('Проверка выхода из аккаунта')
    def test_exit_from_personal_cabinet_success(self, setup_driver, create_and_delete_user):
        driver = AutorizationMethod(setup_driver)
        driver.autorization_by_user()
        driver = MainPage(setup_driver)
        driver.click_to_element(LocatorsMainPage.PERSONAL_CABINET_BUTTON)
        driver.click_to_element(LocatorsPersonalCabinet.EXIT_BUTTON)
        driver.find_element_with_wait(LocatorsLoginPage.PASS_RECOVER_LINK)
        assert driver.get_link() == f'{Data.SITE_URL}{Data.LOGIN_PAGE}'
