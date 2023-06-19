from rest_framework import serializers
from loans.models import Loans

class LoansListRetrieveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Loans
        fields = (
            "id",
            "name",
            "cpf",
            "address",
            "value",
        )
        ref_name = "LoansList"

class LoansCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loans
        fields = (
            "name",
            "cpf",
            "address",
            "value"
        )
        ref_name = "LoansCreate"
    
    def validate(self, attrs):
        if attrs.get('value') != None and attrs.get('value') <= 0:
            raise serializers.ValidationError({"value": "Digite um valor maior igual a 0!"}) 
        return super().validate(attrs)