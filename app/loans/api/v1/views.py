import logging
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from loans.models import Loans
from loans.api.v1.serializers import LoansListRetrieveSerializer, LoansCreateSerializer
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from loans.api.v1 import docs

@method_decorator(name="list", decorator=swagger_auto_schema(**docs.loan_list_docs))
@method_decorator(name="retrieve", decorator=swagger_auto_schema(**docs.loan_retrieve_docs))
@method_decorator(name="create", decorator=swagger_auto_schema(**docs.loan_create_docs))
class LoansView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Loans.objects.all().order_by('id')

    def get_serializer_class(self):
        if self.action in ["create"]:
            return LoansCreateSerializer
        return LoansListRetrieveSerializer

    __basic_fields = [
        "name",
        "address"
    ]

    permission_classes = [
        IsAuthenticated,
    ]

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )

    filterset_fields = __basic_fields
    search_fields = __basic_fields
    ordering_fields = __basic_fields
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)