from django.contrib import admin
from loans.models import Loans


@admin.register(Loans)
class LoansAdmin(admin.ModelAdmin):
    verbose_name = "Loans"
    verbose_name_plural = "Loans"
    model = Loans
    search_fields = ("name",)
    list_display = ("name", "cpf", "address", "value",)