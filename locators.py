from selenium.webdriver.common.by import By

from data import AD_TITLE


class HeaderLocators:
    # Кнопка «Вход и регистрация» в шапке
    LOGIN_AND_REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
    # Кнопка «Разместить объявление» в шапке
    PLACE_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")
    # Аватар авторизованного пользователя
    USER_AVATAR = (By.XPATH, "//button[@class='circleSmall']")
    # Имя авторизованного пользователя
    USER_NAME = (By.XPATH, "//h3[@class='profileText name']")
    # Кнопка «Выйти»
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")


class AuthPopupLocators:
    # Заголовок модального окна авторизации / регистрации
    POPUP_TITLE = (By.XPATH, "//form[contains(@class, 'popUp_shell')]//h1")
    # Поле Email
    EMAIL_INPUT = (By.NAME, 'email')
    # Поле «Пароль»
    PASSWORD_INPUT = (By.NAME, 'password')
    # Поле «Повторите пароль»
    REPEAT_PASSWORD_INPUT = (By.NAME, 'submitPassword')
    # Кнопка «Войти»
    SUBMIT_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Кнопка «Нет аккаунта»
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
    # Кнопка «Создать аккаунт»
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    # Рамка поля Email в состоянии ошибки
    EMAIL_ERROR_FRAME = (
        By.XPATH, "//input[@name='email']/parent::div[contains(@class, 'input_inputError')]")
    # Рамка поля «Пароль» в состоянии ошибки
    PASSWORD_ERROR_FRAME = (
        By.XPATH, "//input[@name='password']/parent::div[contains(@class, 'input_inputError')]")
    # Рамка поля «Повторите пароль» в состоянии ошибки
    REPEAT_PASSWORD_ERROR_FRAME = (
        By.XPATH, "//input[@name='submitPassword']/parent::div[contains(@class, 'input_inputError')]")
    # Сообщение об ошибке под полем Email
    EMAIL_ERROR_MESSAGE = (
        By.XPATH, "//input[@name='email']/ancestor::div[2]/following-sibling::span[contains(@class, 'input_span')]")


class AdFormLocators:
    # Поле «Название»
    TITLE_INPUT = (By.NAME, 'name')
    # Поле «Описание товара»
    DESCRIPTION_INPUT = (By.XPATH, "//textarea[@name='description']")
    # Поле «Стоимость»
    PRICE_INPUT = (By.NAME, 'price')
    # Кнопка раскрытия Dropdown «Категория»
    CATEGORY_DROPDOWN = (By.XPATH, "//input[@name='category']/following-sibling::button")
    # Пункт «Книги» в Dropdown «Категория»
    CATEGORY_OPTION = (By.XPATH, "//button[.//span[text()='Книги']]")
    # Кнопка раскрытия Dropdown «Город»
    CITY_DROPDOWN = (By.XPATH, "//input[@name='city']/following-sibling::button")
    # Пункт «Санкт-Петербург» в Dropdown «Город»
    CITY_OPTION = (By.XPATH, "//button[.//span[text()='Санкт-Петербург']]")
    # RadioButton «Состояние товара» — «Б/У»
    CONDITION_USED_RADIO = (By.XPATH, "//input[@name='condition' and @value='Б/У']/following-sibling::div")
    # Кнопка «Опубликовать»
    PUBLISH_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")


class ProfileLocators:
    # Заголовок блока «Мои объявления»
    MY_ADS_TITLE = (By.XPATH, "//h1[text()='Мои объявления']")
    # Карточка созданного объявления в блоке «Мои объявления»
    CREATED_AD_CARD_TITLE = (
        By.XPATH,
        f"//h1[text()='Мои объявления']/following-sibling::div//div[@class='card']//h2[text()='{AD_TITLE}']")
