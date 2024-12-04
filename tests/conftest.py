import requests
import pytest
from data import Data
from selenium import webdriver



@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def setup_driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    driver.get(Data.SITE_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def create_and_delete_user():
    response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", json=Data.TEST_USER)
    yield
    response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/login", json=Data.TEST_USER)
    r = response.json()
    access_token = r["accessToken"]
    headers = {'Authorization': f'{access_token}'}
    response = requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)