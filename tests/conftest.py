import os
import pytest
from dotenv import load_dotenv

@pytest.fixture(scope='session', autouse=True)
def set_env_vars():
    # Load the .env file
    load_dotenv()