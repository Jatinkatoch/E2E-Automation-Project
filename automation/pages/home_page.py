from config import BASE_URL


class HomePage:

    def __init__(self, page):

        self.page = page

        self.search_box = page.locator("#search")

        self.products = page.locator(".product")

        self.product_cards = page.locator(".card")


    def open(self):

        self.page.goto(
            BASE_URL,
            wait_until="domcontentloaded"
        )


    def search_product(self, product_name):

        self.search_box.fill(product_name)


    def get_product_count(self):

        return self.products.count()


    def click_view_product(self, product_name):

        self.page.locator(
            ".card",
            has_text=product_name
        ).get_by_text(
            "View Details"
        ).click(
            no_wait_after=True
        )

        self.page.wait_for_url(
            "**/product/**",
            wait_until="domcontentloaded"
        )


    def add_product_to_cart(self, product_id):

        self.page.goto(
            f"{BASE_URL}/add/{product_id}"
        )