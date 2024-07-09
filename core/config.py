import os
from dotenv import load_dotenv

load_dotenv()


def read_api_key():
    return os.getenv("API_KEY", default="")


API_KEY = read_api_key()
print(API_KEY)
