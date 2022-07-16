import time

from Pages.PageObject import PageObject


from selenium.webdriver.common.by import By


class ProductNotFoundException(Exception):
    pass


class ProductsPage(PageObject):
    class_product_item = 'sc-iyyVIK.gdPMEf'

    class_product_name = 'sc-iNpzLj.kewvRW'
    class_add_to_cart_btn = 'sc-iNpzLj.kewvRW'

    class_adding_to_cart = 'sc-ikJyIC.eFIXDc.sc-dvXDii.kiHfhN'

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver=driver)

    def choose_product_to_cart(self, product_name):
        all_products = self.driver.find_elements(By.CLASS_NAME, self.class_product_item)

        for product_item in all_products:
            product_item_name = product_item.find_element(By.CLASS_NAME, self.class_product_name).text
            if product_item_name == product_name:
                product_item.find_element(By.CLASS_NAME, self.class_add_to_cart_btn).click()
            break
        else:
            raise ProductNotFoundException(f'Product {product_name} not found!')

    def add_product_cart(self):
        self.driver.find_element(By.CLASS_NAME, self.class_adding_to_cart).click()