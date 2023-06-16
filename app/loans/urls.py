from django.urls import include, path
from loans.api import urls

urlpatterns = [path('api/', include(urls))]