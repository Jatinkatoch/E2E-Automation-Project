class CheckoutPage:


    def __init__(self, page):

        self.page = page


        self.name_input = page.locator(
            'input[name="name"]'
        )


        self.email_input = page.locator(
            'input[name="email"]'
        )


        self.phone_input = page.locator(
            'input[name="phone"]'
        )


        self.address_input = page.locator(
            'textarea[name="address"]'
        )


        self.place_order_button = page.get_by_role(
            "button",
            name="Place Order"
)


        self.success_message = page.locator(
            "h1"
        )



    def fill_customer_details(
        self,
        name,
        email,
        phone,
        address
    ):

        self.name_input.fill(name)

        self.email_input.fill(email)

        self.phone_input.fill(phone)

        self.address_input.fill(address)



    def place_order(self):

        self.place_order_button.click()



    def get_success_message(self):

        return self.success_message.text_content()