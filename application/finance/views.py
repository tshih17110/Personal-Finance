from django.shortcuts import render

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

# Create your views here.

class PlaidLinkViewSet(GenericViewSet):
    @transaction.atomic()
    def create(self, request: Request) -> Response:
        public_token = request.data['public_token']
        exchange = plaid_client.Item.public_token.exchange(public_token)
        token, created = PlaidToken.objects.get_or_create(
            user=request.user,
            defaults={'access_token': exchange['access_token']}
        )
        if not created:
            token.access_token = exchange['access_token']
            token.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
