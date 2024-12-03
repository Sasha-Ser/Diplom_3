import pytest
import allure
from selenium import webdriver

from data import Data
from locators.locators_main_page import LocatorsMainPage
from locators.locators_pass_recovery_page import LocatorsPassRecovery
from locators.locators_login_page import LocatorsLoginPage
from pages.main_page import MainPage


class TestPassRecovery:
    @allure.title('Проверка перехода на страницу с восстановлением пароля')
    def test_go_to_pass_recovery_page_success(self, setup_driver):
        driver = MainPage(setup_driver)
        driver.click_to_element(LocatorsMainPage.PERSONAL_CABINET_BUTTON)
        driver.find_element_with_wait(LocatorsLoginPage.PASS_RECOVER_LINK)
        driver.click_to_element(LocatorsLoginPage.PASS_RECOVER_LINK)
        assert driver.get_link() == f'{Data.SITE_URL}{Data.FORGOT_PASS_PAGE}'

    @allure.title('Проверка перехода на страницу после отправки пароля')
    def test_send_mail_success(self, setup_driver):
        driver = MainPage(setup_driver)
        driver.click_to_element(LocatorsMainPage.PERSONAL_CABINET_BUTTON)
        driver.find_element_with_wait(LocatorsLoginPage.PASS_RECOVER_LINK)
        driver.click_to_element(LocatorsLoginPage.PASS_RECOVER_LINK)
        driver.add_text_to_element(LocatorsPassRecovery.EMAIL_FIELD, "test@yandex.ru")
        driver.click_to_element(LocatorsPassRecovery.BUTTON_RECOVERY)
        driver.find_element_with_wait(LocatorsPassRecovery.BUTTON_SAVE)
        assert driver.get_link() == f'{Data.SITE_URL}{Data.RESET_PASS_PAGE}'

    @allure.title('Проверка активности поля после клика на иконку глазика')
    def test_change_type_filed_success(self, setup_driver):
        driver = MainPage(setup_driver)
        driver.click_to_element(LocatorsMainPage.PERSONAL_CABINET_BUTTON)
        driver.find_element_with_wait(LocatorsLoginPage.PASS_RECOVER_LINK)
        driver.click_to_element(LocatorsLoginPage.PASS_RECOVER_LINK)
        driver.add_text_to_element(LocatorsPassRecovery.EMAIL_FIELD, "test@yandex.ru")
        driver.click_to_element(LocatorsPassRecovery.BUTTON_RECOVERY)
        driver.find_element_with_wait(LocatorsPassRecovery.BUTTON_SAVE)
        driver.click_to_element(LocatorsPassRecovery.CHANGE_VIEW)
        expected_type = 'text'
        assert expected_type in driver.find_element_with_wait(LocatorsPassRecovery.PASSWORD_FIELD).get_attribute('type')