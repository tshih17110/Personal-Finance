import os
import json

from django.shortcuts import render
from django.http import JsonResponse
from django.http import QueryDict
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from dotenv import load_dotenv

import plaid
from plaid.exceptions import ApiException
from plaid.api import plaid_api
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.products import Products
from plaid.model.country_code import CountryCode
from .plaid_config import PlaidConfig

from authentication.models import PlaidToken

# load_dotenv()

# configuration = plaid.Configuration(
#     host=plaid.Environment.Sandbox,
#     api_key={
#         'clientId': os.getenv('PLAID_CLIENT_ID'),
#         'secret': os.getenv('PLAID_SECRET')
#     }
# )

# api_client = plaid.ApiClient(configuration)
# client = plaid_api.PlaidApi(api_client)
plaid_config = PlaidConfig(plaid.Environment.Sandbox)
client = plaid_config.client()

def index(request):
    context = {}
    return render(request, "index.html", context)


@csrf_exempt
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_link_token(request):
    try:
        user_id = settings.PLAID_CLIENT_ID
        plaid_request = LinkTokenCreateRequest(
            products=[Products("transactions")],
            client_name="Personal Finance App",
            country_codes=[CountryCode('CA')],
            language='en',
            user=LinkTokenCreateRequestUser(
                client_user_id=user_id
            )
        )
        response = client.link_token_create(plaid_request)
        return JsonResponse(response.to_dict())
    except plaid.ApiException as e:
        return json.dumps(e.body)

@csrf_exempt
def exchange_public_token(request):
    try:
        public_token = json.loads(request.body.decode('utf-8'))['public_token']
        plaid_request = ItemPublicTokenExchangeRequest(public_token=public_token)
        response = client.item_public_token_exchange(plaid_request)
        access_token = response['access_token']
        item_id = response['item_id']
        os.environ['ACCESS_TOKEN'] = access_token
        os.environ['ITEM_ID'] = item_id
        return JsonResponse(response.to_dict())
    except plaid.ApiException as e:
        return json.dumps(e.body)