import time

import pytest

from Pages.StartPage import StartPage
from Pages.ProductPage import ProductsPage
from Pages.CartPage import CartPage


class Test:

    @pytest.fixture()
    def setup(self):
        # First Step
        self.start_page = StartPage(browser='chrome')
        self.start_page.open_shop_page()
        self.products_page = ProductsPage(self.start_page.driver)
        assert self.start_page.is_url_page(), 'Page was not found'
        yield
        print('Close Browser')
        self.start_page.close()

    def test_click_item(self, setup):
        # Second Step
        print('\n Find a product')
        self.start_page.search_product()
        time.sleep(2)

        # Third step
        print('Validated search')
        assert not self.start_page.is_url_page(), 'Page was not found'

        # Fourth step
        print('Choosing a Product')
        product_1 = 'Usado: iPhone X 256GB Cinza Espacial Excelente - Trocafone - Apple'
        self.products_page.choose_product_to_cart(product_1)
        time.sleep(4)

        # Fifth step
        print('Adding to cart')
        self.products_page.add_product_cart()
        time.sleep(4)

        # Sixth step
        print('Verify if product is in cart')
        time.sleep(2)
        self.cart_page = CartPage(self.products_page.driver)
        assert self.cart_page.is_cart_page(), 'Cart page do not found'
