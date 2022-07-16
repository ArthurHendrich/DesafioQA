from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class StartPage(PageObject):
    URL = 'https://www.magazineluiza.com.br/'

    # Page elements
    product_name = 'Iphone X'
    class_page_logo = 'sc-dkPtRN.loCDsW'
    id_input_text = 'input-search'
    class_send_input = 'sc-dkPtRN.kkxyKb'

    def __init__(self, browser):
        super(StartPage, self).__init__(browser=browser)
        self.open_shop_page()

    def open_shop_page(self):
        self.driver.get(self.URL)

    def is_url_page(self):
        is_url_page = self.driver.current_url == self.URL
        try:
            is_logo = self.driver.find_element(By.CLASS_NAME, self.class_page_logo)
        except NoSuchElementException:
            is_logo = False

        return is_url_page and is_logo

    def search_product(self):
        self.driver.find_element(By.ID, self.id_input_text).send_keys(self.product_name)
        self.driver.find_element(By.CLASS_NAME, self.class_send_input).click()
