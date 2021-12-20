from rest_framework import serializers
from .models import Contract
from syans_server.serializers import UserSerializer

class ContractSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only=True)
    executor = UserSerializer(read_only=True)
    class Meta:
        model = Contract
        fields = ['id', 'title', 'task', 'customer', 'executor', 'cost', 'status']
