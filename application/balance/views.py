import json

from django.shortcuts import render
from plaid.exceptions import ApiException
from plaid.model.accounts_balance_get_request import AccountsBalanceGetRequest
from plaid.model.accounts_get_response import AccountsGetResponse
from .plaid_config import PlaidConfig

def accounts_balance_get():
    try:
        plaid_config = PlaidConfig(plaid.Environment.Sandbox)
        client = plaid_config.client()

        # request = AccountsBalanceGetRequest()
         
    except ApiException as e:
        return json.dumps(e.body)
