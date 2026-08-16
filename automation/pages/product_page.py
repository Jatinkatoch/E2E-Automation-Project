class ProductPage:


    def __init__(self, page):

        self.page = page


        self.product_name = page.locator(
            "h1"
        )


        self.product_price = page.locator(
            "h3"
        )


        self.product_description = page.locator(
            "p"
        )


        self.add_cart_button = page.get_by_text(
            "Add To Cart"
        )



    def get_product_name(self):

        return self.product_name.text_content()



    def get_product_price(self):

        return self.product_price.text_content()



    def add_to_cart(self):

        self.add_cart_button.click()