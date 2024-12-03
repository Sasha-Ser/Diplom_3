import allure
import selenium
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderFeedPage(BasePage):

    @allure.step('Поиск элемента из множества')
    def find_element_among_set_with_wait(self, locator, order):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(
            locator))
        orders = self.driver.find_elements(*locator)
        for i in orders:
            if order in i.text:
                return True
        return False