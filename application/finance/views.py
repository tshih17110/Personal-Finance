import os

from django.shortcuts import render
from django.http import JsonResponse
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
from plaid.model.products import Products
from plaid.model.country_code import CountryCode

from finance.models import PlaidToken

load_dotenv()

configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': os.getenv('PLAID_CLIENT_ID'),
        'secret': os.getenv('PLAID_SECRET')
    }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)


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
            country_codes=[CountryCode('US')],
            language='en',
            user=LinkTokenCreateRequestUser(
                client_user_id=user_id
            )
        )
        response = client.link_token_create(plaid_request)
        return JsonResponse(response.to_dict())
    except plaid.ApiException as e:
        return json.dumps(e.body)

