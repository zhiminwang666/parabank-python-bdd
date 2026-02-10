import os
from dotenv import load_dotenv

load_dotenv() # load environment variables from .env file

BASE_UI_URL = os.getenv("BASE_UI_URL", "https://parabank.parasoft.com/parabank/index.htm")
BASE_API_URL = os.getenv("BASE_API_URL", "https://parabank.parasoft.com/parabank/services_proxy/bank")

USERNAME = os.getenv("PB_USERNAME", "john")
PASSWORD = os.getenv("PB_PASSWORD", "demo")
BROWSER = os.getenv("BROWSER", "chrome")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
