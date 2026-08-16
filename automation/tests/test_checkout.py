from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.test_data import TestData



def test_checkout_page_load(page):

    login = LoginPage(page)

    login.open()

    login.login(
        "test@gmail.com",
        "Test@12345"
    )


    home = HomePage(page)

    home.open()

    home.click_view_product(
        "Gaming Laptop"
    )


    product = ProductPage(page)

    product.add_to_cart()


    cart = CartPage(page)

    cart.proceed_checkout()


    assert "/order" in page.url



def test_place_order_success(page):

    login = LoginPage(page)

    login.open()

    login.login(
        "test@gmail.com",
        "Test@12345"
    )


    home = HomePage(page)

    home.open()

    home.click_view_product(
        "Gaming Laptop"
    )


    product = ProductPage(page)

    product.add_to_cart()


    cart = CartPage(page)

    cart.proceed_checkout()


    checkout = CheckoutPage(page)


    checkout.fill_customer_details(
          TestData.user_name(),
          TestData.user_email(),
          TestData.phone(),
          TestData.address()
    )


    checkout.place_order()


    message = checkout.get_success_message()


    assert "Order" in message