from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            'Items in the basket, but should not be'

    def should_be_message_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_TEXT_EMPTY), \
            'Messsage "basket is empty" is not presented, but should be'
