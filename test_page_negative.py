import pytest

from .pages.product_page import ProductPage

link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209"


@pytest.mark.xfail(reason="success message is presented")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="success message is not disappeared")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_have_disappeard()
