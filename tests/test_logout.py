from selenium.webdriver.support import expected_conditions as EC

from data import LOGIN_BUTTON_TEXT
from locators import HeaderLocators


class TestLogout:

    def test_logout_hides_user_avatar_and_name_and_shows_login_button(self, authorized_driver, wait):
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGOUT_BUTTON)).click()

        login_button = wait.until(EC.visibility_of_element_located(HeaderLocators.LOGIN_AND_REGISTRATION_BUTTON))
        avatars = authorized_driver.find_elements(*HeaderLocators.USER_AVATAR)
        user_names = authorized_driver.find_elements(*HeaderLocators.USER_NAME)

        assert avatars == [] and user_names == [] and login_button.text == LOGIN_BUTTON_TEXT
