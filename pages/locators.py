from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD_1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD_2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_SUBMIT_BTN = (By.CSS_SELECTOR, '#register_form > button')


class ProductPageLocators():
    BASKET_ADD_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main > h1')
    NAME_BASKET = (By.CSS_SELECTOR, '#messages .alert-success:nth-child(1) strong')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.price_color')
    PRICE_BASKET = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1)')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LOOK_BTN = (By.CSS_SELECTOR, ".btn-group a")
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, '#basket_formset > div')
    BASKET_TEXT_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')
