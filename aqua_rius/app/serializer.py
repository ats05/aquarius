from rest_framework import serializers
from app.models import Apikey

class ApikeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apikey
