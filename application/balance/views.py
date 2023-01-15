import json
import os

from dotenv import load_dotenv
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import plaid
from plaid.exceptions import ApiException
from plaid.model.accounts_balance_get_request import AccountsBalanceGetRequest
from plaid.model.accounts_get_response import AccountsGetResponse
from authentication.plaid_config import PlaidConfig

@csrf_exempt
def accounts_balance_get(request):
    try:
        plaid_config = PlaidConfig(plaid.Environment.Sandbox)
        client = plaid_config.client()
        plaid_request = AccountsBalanceGetRequest(os.getenv('ACCESS_TOKEN'))
        response = client.accounts_balance_get(plaid_request)
        return JsonResponse(response.to_dict())
         
    except ApiException as e:
        return json.dumps(e.body)
