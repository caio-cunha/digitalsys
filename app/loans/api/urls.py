from django.urls import include, path
from loans.api.v1 import urls

urlpatterns = [path("v1/", include(urls))]