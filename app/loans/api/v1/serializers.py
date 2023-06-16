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