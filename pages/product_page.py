from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_basket_button()

    def should_be_product_url(self):
        assert "?promo=newYear" in self.browser.current_url, "not correct url"

    def should_be_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_BTN), "basket_btn is not presented"

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BTN).click()