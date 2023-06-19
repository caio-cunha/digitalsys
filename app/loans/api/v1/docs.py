from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema
from rest_framework import status
from . import serializers


class LoansAutoSchema(SwaggerAutoSchema):
    def get_tags(self, operation_keys):
        return ['Loans']
    

loan_retrieve_docs = {
    "auto_schema": LoansAutoSchema,
    "operation_summary": 'Get one loan',
    "responses": {
        status.HTTP_200_OK: serializers.LoansListRetrieveSerializer,
        status.HTTP_400_BAD_REQUEST: '{"error": [message]}',
        status.HTTP_401_UNAUTHORIZED: '{"error": [message]}',
    },
}

loan_list_docs = {
    "auto_schema": LoansAutoSchema,
    "operation_summary": 'List all loans',
    "responses": {
        status.HTTP_200_OK: serializers.LoansListRetrieveSerializer,
        status.HTTP_400_BAD_REQUEST: '{"error": [message]}',
        status.HTTP_401_UNAUTHORIZED: '{"error": [message]}',
    },
}

loan_create_docs = {
    "auto_schema": LoansAutoSchema,
    "operation_summary": 'Save one loan',
    "responses": {
        status.HTTP_201_CREATED: serializers.LoansCreateSerializer,
        status.HTTP_400_BAD_REQUEST: '{"error": [message]}',
        status.HTTP_401_UNAUTHORIZED: '{"error": [message]}',
        status.HTTP_404_NOT_FOUND: '{"error": [message]}',
    },
}