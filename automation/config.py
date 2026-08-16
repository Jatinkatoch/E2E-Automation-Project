import os

BASE_URL = os.getenv(
    "BASE_URL",
    "http://ecommerce-app:5000"      #os.get(variable_name,default_value)
)


# BASE_URL = os.getenv(
#     "BASE_URL",
#     "http://127.0.0.1:5000"
# )