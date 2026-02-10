import requests
from config.settings import BASE_API_URL

class ParaBankApi:
    def __init__(self):
        self.session = requests.Session()

    def create_account(self, customer_id: int, new_account_type: int, from_account_id: int) -> dict:
        url = f"{BASE_API_URL}/createAccount"
        params = {
            "customerId": customer_id,
            "newAccountType": new_account_type,
            "fromAccountId": from_account_id
        }
        r = self.session.post(url, params=params, timeout=10)
        r.raise_for_status()
        return r.json()  # data handling: json -> dict
