import pytest
import logging as logger

from scr.pages.HomePage import HomePage
from scr.pages.CartPage import CartPage
from scr.pages.CheckoutPage import CheckoutPage
from scr.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestComponentFooter:

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.checkout = CheckoutPage(self.driver)
        request.cls.myacc = MyAccountSignedOut(self.driver)
        yield

    @pytest.mark.ecomfe50
    def test_demostore_displayed_on_footer(self, setup):
        logger.info(f"Running Test: test_demostore_displayed_on_footer")
        self.homepage.go_to_home_page()
        demo_ecom_store = self.homepage.get_displayed_company_name()
        # Assert that searching not existing product returned right message
        assert demo_ecom_store == '© Demo eCom Store 2023\nBuilt with Storefront & WooCommerce.','page does not have © Demo eCom Store 2023 displayed'

    @pytest.mark.ecomfe51
    def test_footer_displayed_on_every_page(self,setup):
        logger.info(f"Running Test: test_footer_displayed_on_every_page")
        listx = [ self.homepage.go_to_home_page,self.cart.go_to_cart_page,self.checkout.go_to_checkout_page,self.myacc.go_to_my_account]
        for i in listx:
            i()
            demo_ecom_store = self.homepage.get_displayed_company_name()
            # Assert that searching not existing product returned right message
            assert demo_ecom_store == '© Demo eCom Store 2023\nBuilt with Storefront & WooCommerce.', 'page does not have © Demo eCom Store 2023 displayed'

    @pytest.mark.ecomfe52
    def test_footer_has_link_to_woocomerce(self,setup):
        logger.info(f"Running Test: test_footer_has_link_to_woocomerce")
        listx = [self.homepage.go_to_home_page, self.cart.go_to_cart_page, self.checkout.go_to_checkout_page,
                 self.myacc.go_to_my_account]
        for i in listx:
            i()
            woocomerce = self.homepage.get_woocommerce_link_from_footer()
            # Assert that searching not existing product returned right message
            assert woocomerce == 'Built with Storefront & WooCommerce', 'page does not have © Demo eCom Store 2023 displayed'

