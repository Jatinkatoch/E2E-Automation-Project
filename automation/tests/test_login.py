from pages.login_page import LoginPage
from utils.test_data import TestData
from config import BASE_URL


def test_valid_login(page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        TestData.user_email(),
        TestData.password()
    )

    assert page.url == f"{BASE_URL}/"



def test_invalid_login(page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        "wrong@gmail.com",
        "wrongpassword"
    )

    error_message = page.locator(
        ".alert-danger"
    )

    assert error_message.is_visible()



def test_login_with_dynamic_email(page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        TestData.user_email(),
        TestData.password()
    )

    # assert page.url == "http://127.0.0.1:5000/"
    assert page.url == f"{BASE_URL}/"