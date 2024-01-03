import time

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


@pytest.mark.mytest1
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        self.product_link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        self.link = 'https://selenium1py.pythonanywhere.com/ru/'
        page = LoginPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        email = str(time.time()) + 'xaxa@pochta.ru'
        password = 'adjDF454335DFHTtgffkd'
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.product_link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.product_link)
        page.open()
        page.should_be_product_page()
        page.add_to_basket()
        page.solve_quiz_and_get_code()


@pytest.mark.need_review
@pytest.mark.parametrize('link', [
    link if link != 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7'
    else pytest.param(link, marks=pytest.mark.xfail) for link in links])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.solve_quiz_and_get_code()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_message_empty()
