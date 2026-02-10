import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from config.settings import HEADLESS

@pytest.fixture
def driver():
    options = Options() # this is for Chrome; for Firefox, use webdriver.FirefoxOptions()
    if HEADLESS:
        options.add_argument("--headless=new") # for Chrome 109+; for older versions, use "--headless"
    options.add_argument("--window-size=1280,800") # set a fixed window size for consistency; adjust as needed

    svc = Service(ChromeDriverManager().install()) # automatically download and manage ChromeDriver; for Firefox, use GeckoDriverManager
    d = webdriver.Chrome(service=svc, options=options)
    # we'll use explicit waits instead of implicit waits for better control and reliability
    d.implicitly_wait(0)
    # this will return the driver to the test function,
    # and after the test finishes, it will continue to the next line
    yield d
    d.quit()

@pytest.fixture
def wait(driver):
    # I avoid hard sleep; I use explicit wait via WebDriverWait.
    return WebDriverWait(driver, 10)