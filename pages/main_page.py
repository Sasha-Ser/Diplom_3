import allure
import selenium
from selenium import webdriver
from pages.base_page import BasePage
from data import Data
from locators.locators_main_page import LocatorsMainPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):

    @allure.step('Ожидание удаления элемента')
    def wait_for_disappear(self, locator):
        elements = self.driver.find_elements(*locator)
        if elements:
            WebDriverWait(self.driver, Data.TIME_WAIT).until(expected_conditions.invisibility_of_element(elements[0]))

        return True

    @allure.step('Перетаскивание элемента')
    def drag_and_drop(self, locator_from, locator_to):
        if isinstance(self.driver, webdriver.Chrome):
            locator_from = self.driver.find_element(*locator_from)
            locator_to = self.driver.find_element(*locator_to)
            actions = ActionChains(self.driver)
            actions.click_and_hold(locator_from).move_to_element(locator_to).release().perform()
        else:
            self.find_element_with_wait(locator_from)
            self.find_element_with_wait(locator_to)
            element_from = self.driver.find_element(*locator_from)
            element_to = self.driver.find_element(*locator_to)
            self.driver.execute_script("""
                    var source = arguments[0];
                    var target = arguments[1];
                    var evt = document.createEvent("DragEvent");
                    evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                    source.dispatchEvent(evt);
                    evt = document.createEvent("DragEvent");
                    evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                    target.dispatchEvent(evt);
                    evt = document.createEvent("DragEvent");
                    evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                    target.dispatchEvent(evt);
                    evt = document.createEvent("DragEvent");
                    evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                    target.dispatchEvent(evt);
                    evt = document.createEvent("DragEvent");
                    evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                    source.dispatchEvent(evt);""", element_from, element_to)

    @allure.step('Ожидание изменение текста')
    def wait_for_change_text(self, locator, value):
        WebDriverWait(self.driver, Data.TIME_WAIT).until(
            lambda driver: self.get_text_from_element (locator) != value)#d.(*locator).text != value)
        return True

    @allure.step('Создание определенного заказа')
    def creation_order(self):
        self.find_element_with_wait(LocatorsMainPage.BUN_FOR_BURGER)
        self.drag_and_drop(LocatorsMainPage.BUN_FOR_BURGER, LocatorsMainPage.CONSTRUCTOR_BURGER)
        self.click_to_element(LocatorsMainPage.CREATE_ORDER_BUTTON)
        self.wait_for_change_text(LocatorsMainPage.ID_ORDER, "9999")
        order_id = self.get_text_from_element(LocatorsMainPage.ID_ORDER)
        self.click_to_element(LocatorsMainPage.CLOSE_INFO_ORDER_BUTTON)
        return order_id
