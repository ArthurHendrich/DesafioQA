from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class CartPage(PageObject):

    class_page_title = 'BasketPage-title'
    class_checkout_btn = 'BasketContinue-button'

    class_cart_item = 'BasketItemProduct-info-title'

    def __init__(self, driver):
        super(CartPage, self).__init__(driver=driver)

    def is_cart_page(self):
        try:
            element_class_title = self.driver.find_element(By.CLASS_NAME, self.class_page_title)
            btn_checkout = self.driver.find_element(By.CLASS_NAME, self.class_checkout_btn)
            return element_class_title and btn_checkout
        except NoSuchElementException:
            return False

