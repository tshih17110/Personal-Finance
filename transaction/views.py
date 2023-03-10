import json
import os

# from datetime import datetime
import datetime
from dateutil.relativedelta import relativedelta
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import plaid
from plaid.exceptions import ApiException
from plaid.model.transactions_sync_request import TransactionsSyncRequest
from plaid.model.transactions_get_request import TransactionsGetRequest
from plaid.model.transactions_get_response import TransactionsGetResponse
from plaid.model.transactions_get_request_options import TransactionsGetRequestOptions
from authentication.plaid_config import PlaidConfig

plaid_config = PlaidConfig(plaid.Environment.Sandbox)
plaid_client = plaid_config.client()



@csrf_exempt
def get_transactions(request):
    plaid_request = TransactionsGetRequest(
        access_token = os.getenv('ACCESS_TOKEN'),
        start_date = (datetime.date.today() - relativedelta(months=1)),
        end_date = datetime.date.today(),
    )
    response = plaid_client.transactions_get(plaid_request)
    transactions = response['transactions']
    return JsonResponse(response.to_dict())


    
