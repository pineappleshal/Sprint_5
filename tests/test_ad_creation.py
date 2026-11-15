from selenium.webdriver.support import expected_conditions as EC

from data import AD_DESCRIPTION, AD_PRICE, AD_TITLE, BASE_URL, UNAUTHORIZED_MODAL_TITLE
from locators import AdFormLocators, AuthPopupLocators, HeaderLocators, ProfileLocators


class TestAdCreation:

    def test_place_ad_by_unauthorized_user_shows_authorization_modal(self, driver, wait):
        wait.until(EC.element_to_be_clickable(HeaderLocators.PLACE_AD_BUTTON)).click()

        modal_title = wait.until(EC.visibility_of_element_located(AuthPopupLocators.POPUP_TITLE))

        assert modal_title.text == UNAUTHORIZED_MODAL_TITLE

    def test_place_ad_by_authorized_user_shows_ad_in_profile(self, authorized_driver, wait):
        wait.until(EC.element_to_be_clickable(HeaderLocators.PLACE_AD_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AdFormLocators.TITLE_INPUT)).send_keys(AD_TITLE)
        authorized_driver.find_element(*AdFormLocators.DESCRIPTION_INPUT).send_keys(AD_DESCRIPTION)
        authorized_driver.find_element(*AdFormLocators.PRICE_INPUT).send_keys(AD_PRICE)
        authorized_driver.find_element(*AdFormLocators.CATEGORY_DROPDOWN).click()
        wait.until(EC.element_to_be_clickable(AdFormLocators.CATEGORY_OPTION)).click()
        authorized_driver.find_element(*AdFormLocators.CITY_DROPDOWN).click()
        wait.until(EC.element_to_be_clickable(AdFormLocators.CITY_OPTION)).click()
        authorized_driver.find_element(*AdFormLocators.CONDITION_USED_RADIO).click()
        authorized_driver.find_element(*AdFormLocators.PUBLISH_BUTTON).click()
        wait.until(EC.url_to_be(BASE_URL))
        wait.until(EC.element_to_be_clickable(HeaderLocators.USER_AVATAR)).click()
        wait.until(EC.visibility_of_element_located(ProfileLocators.MY_ADS_TITLE))

        created_ad_title = wait.until(EC.visibility_of_element_located(ProfileLocators.CREATED_AD_CARD_TITLE))

        assert created_ad_title.text == AD_TITLE
