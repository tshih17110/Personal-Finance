from rest_framework import serializers
from authentication import PlaidToken

class PlaidTokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlaidToken
        fields = ['access_token', 'user']