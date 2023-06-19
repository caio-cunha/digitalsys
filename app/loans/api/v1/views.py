import logging
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets, mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from loans.models import Loans
from loans.api.v1.serializers import LoansListRetrieveSerializer, LoansCreateSerializer

class LoansView(
    mixins.ListModelMixin,
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
    