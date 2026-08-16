from config import BASE_URL
class LoginPage:


    def __init__(self, page):

        self.page = page


        self.email_input = page.locator(
            'input[name="email"]'
        )


        self.password_input = page.locator(
            'input[name="password"]'
        )


        self.login_button = page.locator(
            "button.btn-primary"
        )



    def open(self):

         self.page.goto(
            f"{BASE_URL}/login",
            wait_until="domcontentloaded"
    )
    



    def login(self, email, password):

        self.email_input.fill(email)

        self.password_input.fill(password)

        self.login_button.click()

        self.page.wait_for_timeout(1000)