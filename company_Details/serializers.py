from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from . models import company,contact

class companySerializer(serializers.ModelSerializer):
    class Meta:
        model = company
        fields = '__all__'
class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        fields = '__all__'

