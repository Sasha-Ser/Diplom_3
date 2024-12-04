import allure
import selenium
from selenium import webdriver
from data import Data
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, setup_driver):
        self.driver = setup_driver

    @allure.step('Поиск элемента')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, Data.TIME_WAIT).until(
            expected_conditions.visibility_of_element_located(
            locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу')
    def click_to_element(self, locator):
        if isinstance(self.driver, webdriver.Chrome):
            WebDriverWait(self.driver, Data.TIME_WAIT).until(
                expected_conditions.element_to_be_clickable(locator))
            self.driver.find_element(*locator).click()
        else:
            WebDriverWait(self.driver, Data.TIME_WAIT).until(
                expected_conditions.visibility_of_element_located(locator))
            element = self.find_element_with_wait(locator)
            WebDriverWait(self.driver, Data.TIME_WAIT).until(
                expected_conditions.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Ввод информации')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получение текста из элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Получение ссылки')
    def get_link(self):
        return self.driver.current_url


