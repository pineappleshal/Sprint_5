from selenium.webdriver.support import expected_conditions as EC

from data import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD, USER_NAME
from locators import AuthPopupLocators, HeaderLocators


class TestLogin:

    def test_login_with_valid_data_shows_user_avatar_and_name(self, driver, wait):
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_AND_REGISTRATION_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthPopupLocators.EMAIL_INPUT)).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*AuthPopupLocators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*AuthPopupLocators.SUBMIT_LOGIN_BUTTON).click()

        avatar = wait.until(EC.visibility_of_element_located(HeaderLocators.USER_AVATAR))
        user_name = wait.until(EC.visibility_of_element_located(HeaderLocators.USER_NAME))

        assert avatar.is_displayed() and user_name.text == USER_NAME
