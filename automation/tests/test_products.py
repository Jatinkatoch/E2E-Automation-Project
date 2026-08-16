from utils.test_data import TestData
from pages.home_page import HomePage
from pages.product_page import ProductPage



def test_product_listing(page):


    home_page = HomePage(page)


    home_page.open()


    product_count = home_page.get_product_count()


    assert product_count > 0




def test_open_product_details(page):


    home_page = HomePage(page)


    home_page.open()


    home_page.click_view_product(
        TestData.product()
    )


    product_page = ProductPage(page)


    product_name = product_page.get_product_name()


    assert TestData.product() in product_name




def test_product_price_visible(page):


    home_page = HomePage(page)


    home_page.open()


    home_page.click_view_product(
        TestData.product()
    )


    product_page = ProductPage(page)


    price = product_page.get_product_price()


    assert "₹" in price




def test_add_product_to_cart(page):


    home_page = HomePage(page)


    home_page.open()


    home_page.click_view_product(
        TestData.product()
    )


    product_page = ProductPage(page)


    product_page.add_to_cart()


    assert "/checkout" in page.url