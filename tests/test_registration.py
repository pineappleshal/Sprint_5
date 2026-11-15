from selenium.webdriver.support import expected_conditions as EC

from data import (ERROR_BORDER_COLOR, ERROR_MESSAGE, EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD,
                  INVALID_EMAIL, NEW_USER_PASSWORD, USER_NAME)
from helpers import generate_email
from locators import AuthPopupLocators, HeaderLocators


class TestRegistration:

    def test_registration_with_valid_data_shows_user_avatar_and_name(self, driver, wait):
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_AND_REGISTRATION_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthPopupLocators.NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthPopupLocators.REPEAT_PASSWORD_INPUT))
        driver.find_element(*AuthPopupLocators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*AuthPopupLocators.PASSWORD_INPUT).send_keys(NEW_USER_PASSWORD)
        driver.find_element(*AuthPopupLocators.REPEAT_PASSWORD_INPUT).send_keys(NEW_USER_PASSWORD)
        driver.find_element(*AuthPopupLocators.CREATE_ACCOUNT_BUTTON).click()

        avatar = wait.until(EC.visibility_of_element_located(HeaderLocators.USER_AVATAR))
        user_name = wait.until(EC.visibility_of_element_located(HeaderLocators.USER_NAME))

        assert avatar.is_displayed() and user_name.text == USER_NAME

    def test_registration_with_invalid_email_shows_error(self, driver, wait):
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_AND_REGISTRATION_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthPopupLocators.NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthPopupLocators.REPEAT_PASSWORD_INPUT))
        driver.find_element(*AuthPopupLocators.EMAIL_INPUT).send_keys(INVALID_EMAIL)
        driver.find_element(*AuthPopupLocators.CREATE_ACCOUNT_BUTTON).click()

        wait.until(EC.text_to_be_present_in_element(AuthPopupLocators.EMAIL_ERROR_MESSAGE, ERROR_MESSAGE))
        border_colors = [
            driver.find_element(*AuthPopupLocators.EMAIL_ERROR_FRAME).value_of_css_property('border-color'),
            driver.find_element(*AuthPopupLocators.PASSWORD_ERROR_FRAME).value_of_css_property('border-color'),
            driver.find_element(*AuthPopupLocators.REPEAT_PASSWORD_ERROR_FRAME).value_of_css_property('border-color'),
        ]
        error_text = driver.find_element(*AuthPopupLocators.EMAIL_ERROR_MESSAGE).text

        assert border_colors == [ERROR_BORDER_COLOR] * 3 and error_text == ERROR_MESSAGE

    def test_registration_of_existing_user_shows_error(self, driver, wait):
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_AND_REGISTRATION_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthPopupLocators.NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthPopupLocators.REPEAT_PASSWORD_INPUT))
        driver.find_element(*AuthPopupLocators.EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*AuthPopupLocators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*AuthPopupLocators.REPEAT_PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*AuthPopupLocators.CREATE_ACCOUNT_BUTTON).click()

        wait.until(EC.text_to_be_present_in_element(AuthPopupLocators.EMAIL_ERROR_MESSAGE, ERROR_MESSAGE))
        border_colors = [
            driver.find_element(*AuthPopupLocators.EMAIL_ERROR_FRAME).value_of_css_property('border-color'),
            driver.find_element(*AuthPopupLocators.PASSWORD_ERROR_FRAME).value_of_css_property('border-color'),
            driver.find_element(*AuthPopupLocators.REPEAT_PASSWORD_ERROR_FRAME).value_of_css_property('border-color'),
        ]
        error_text = driver.find_element(*AuthPopupLocators.EMAIL_ERROR_MESSAGE).text

        assert border_colors == [ERROR_BORDER_COLOR] * 3 and error_text == ERROR_MESSAGE
