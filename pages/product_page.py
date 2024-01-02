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
            *ProductPageLocators.BASKET_ADD_BTN), "basket_btn is not presented"

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_ADD_BTN).click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_have_disappeard(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not dissappeard, but should be"
