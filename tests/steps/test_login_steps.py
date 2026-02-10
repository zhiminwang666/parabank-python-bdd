from pytest_bdd import scenarios, given, when, then
from tests.pages.login_page import LoginPage
from tests.utils.retry import retryable
from config.settings import USERNAME, PASSWORD

scenarios("../features/login.feature")

@given("I open the ParaBank login page")
def open_login(driver, wait):
    page = LoginPage(driver, wait)
    page.open()

@when("I login with valid credentials")
def do_login(driver, wait):
    page = LoginPage(driver, wait)
    page.login(USERNAME, PASSWORD)

@then("I should see the logout link")
def assert_logout(driver, wait):
    page = LoginPage(driver, wait)

    # retry workflow: handle eventual consistency / slow UI
    def check():
        assert page.is_logged_in(), "Logout link not visible yet"
        return True

    retryable(check)
