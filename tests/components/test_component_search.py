import time

import pytest
import logging as logger


from scr.pages.HomePage import HomePage
from scr.pages.CartPage import CartPage
from scr.pages.CheckoutPage import CheckoutPage
from scr.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestComponenetSearch:

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.checkout = CheckoutPage(self.driver)
        request.cls.myacc = MyAccountSignedOut(self.driver)
        yield

    @pytest.mark.tcid117
    @pytest.mark.ecomfe49
    def test_searching_not_existing_product(self, setup):
        logger.info(f"Running Test: test_searching_not_existing_product")
        self.homepage.go_to_home_page()
        self.homepage.input_int_search_field(value='doesnotexist')
        self.homepage.press_enter_on_search_field()

        no_product_message = self.homepage.get_no_product_message()

        # Assert that searching not existing product returned right message
        assert no_product_message == 'No products were found matching your selection.', "searching product returned wrong text"

    @pytest.mark.ecomfe47
    def test_search_field_visible_on_every_page(self,setup):
        logger.info(f"Running Test: test_search_field_visible_on_every_page")
        listx = [self.homepage.go_to_home_page, self.cart.go_to_cart_page, self.checkout.go_to_checkout_page,
                 self.myacc.go_to_my_account]
        for i in listx:
            i()
            search = self.homepage.get_search_field()
            # Assert that searching not existing product returned right message
            assert search,'page does not have search field displayed.'

    @pytest.mark.ecomfe48
    def test_search_field_functionl_on_every_page(self,setup):
        logger.info(f"Running Test: test_search_field_functionl_on_every_page")
        listx = [self.homepage.go_to_home_page, self.cart.go_to_cart_page, self.checkout.go_to_checkout_page,
                 self.myacc.go_to_my_account]
        for i in listx:
            i()
            self.homepage.input_int_search_field(value='Beanie')
            self.homepage.press_enter_on_search_field()
            product_message = self.homepage.get_search_result_success_message()

            # Assert that searching not existing product returned right message
            assert product_message =='Search results: “Beanie”', 'search not successful.'

