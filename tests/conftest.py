from selenium import webdriver
import pytest
from data import Data


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def setup_driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    driver.get(Data.SITE_URL)
    yield driver
    driver.quit()