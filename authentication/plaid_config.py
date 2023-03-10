import os
import plaid

from dotenv import load_dotenv
from plaid.api import plaid_api

load_dotenv()

class PlaidConfig():
    def __init__(self, env):
        self.env = env

    def client(self):
        configuration = plaid.Configuration(
            host=self.env,
            api_key={
                'clientId': os.getenv('PLAID_CLIENT_ID'),
                'secret': os.getenv('PLAID_SECRET')
            }
        )
        api_client = plaid.ApiClient(configuration)
        client = plaid_api.PlaidApi(api_client)
        return client