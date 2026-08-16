from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage



def test_cart_has_product(page):

    home = HomePage(page)

    home.open()

    home.click_view_product(
        "Gaming Laptop"
    )

    product = ProductPage(page)

    product.add_to_cart()

    cart = CartPage(page)

    assert cart.get_cart_count() == 1


def test_cart_total(page):

    home = HomePage(page)

    home.open()

    home.click_view_product(
        "Gaming Laptop"
    )

    product = ProductPage(page)

    product.add_to_cart()

    cart = CartPage(page)

    assert "85000" in cart.get_total()


def test_proceed_checkout(page):

    login = LoginPage(page)

    login.open()

    login.login(
        "test@gmail.com",
        "Test@12345"
    )

    home = HomePage(page)

    home.click_view_product(
        "Gaming Laptop"
    )

    product = ProductPage(page)

    product.add_to_cart()

    cart = CartPage(page)

    cart.proceed_checkout()

    assert "/order" in page.url