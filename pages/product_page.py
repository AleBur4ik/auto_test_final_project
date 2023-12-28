import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_basket_button()

    def should_be_product_url(self):
        assert "selenium1py.pythonanywhere.com" in self.browser.current_url, "not correct url"

    def should_be_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_BTN), "basket_btn is not presented"

    def add_to_basket(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        price_product = \
        self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text.split('&')[0]
        self.browser.find_element(*ProductPageLocators.BASKET_BTN).click()
        self.solve_quiz_and_get_code()
        name_basket = self.browser.find_element(*ProductPageLocators.NAME_BASKET).text
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        assert name_basket == name_product, f"Ошибка товара ({name_product} =! {name_basket})"
        assert price_basket == price_product, f"Ошибка цены ({price_product} =! {price_basket})"
        print(f"Товар '{name_product}' добавлен в корзину")
        print(f"Стоимость : {price_product}")
