import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import BASE_URL, DEFAULT_TIMEOUT, EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD
from locators import AuthPopupLocators, HeaderLocators


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.get(BASE_URL)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, DEFAULT_TIMEOUT)


@pytest.fixture
def authorized_driver(driver, wait):
    wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_AND_REGISTRATION_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(AuthPopupLocators.EMAIL_INPUT)).send_keys(EXISTING_USER_EMAIL)
    driver.find_element(*AuthPopupLocators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
    driver.find_element(*AuthPopupLocators.SUBMIT_LOGIN_BUTTON).click()
    wait.until(EC.visibility_of_element_located(HeaderLocators.USER_AVATAR))
    return driver
