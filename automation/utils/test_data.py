from faker import Faker


fake = Faker()


class TestData:


    @staticmethod
    def user_email():
        return "test@gmail.com"


    @staticmethod
    def user_name():
        return fake.name()


    @staticmethod
    def password():
        return "Test@12345"


    @staticmethod
    def product():
        return "Gaming Laptop"


    @staticmethod
    def phone():
        return fake.phone_number()


    @staticmethod
    def address():
        return fake.address()