from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main > h1')
    NAME_BASKET = (By.CSS_SELECTOR, '#messages .alert-success:nth-child(1) strong')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.price_color')
    PRICE_BASKET = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
