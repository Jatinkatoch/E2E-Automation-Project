class CartPage:

    def __init__(self, page):

        self.page = page

        self.cart_rows = page.locator("table tr")

        self.total = page.locator("h2")

        self.checkout_button = page.get_by_role(
            "link",
            name="Proceed Checkout"
        )

    def get_cart_count(self):

        return self.cart_rows.count() - 1

    def get_total(self):

        return self.total.text_content()

    def proceed_checkout(self):

        self.checkout_button.click()

