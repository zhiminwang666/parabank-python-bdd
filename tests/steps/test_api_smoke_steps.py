from pytest_bdd import scenarios, given, then
from tests.api.parabank_api import ParaBankApi

scenarios("../features/api_auth.feature")

@given("I call createAccount API without auth", target_fixture="call_unauth")
def call_unauth():
    api = ParaBankApi()
    return api.create_account_raw(customer_id=12212, new_account_type=0, from_account_id=13344)

@then("API response status should be 401")
def assert_401(call_unauth):
    assert call_unauth.status_code == 401
