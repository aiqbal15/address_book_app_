from django.urls import path
from .views import get_addresses, create_address, address_detail
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path('swagger-docs/', TemplateView.as_view(template_name='docs.html', extra_context={'schema_url':'api_schema'}), name='swagger-ui'),
    path('schema/', get_schema_view(title="Address Book API", description="API Documentation for address book CRUD system"), name='api_schema'),
    path('addresses/', get_addresses, name='get_addresses'),
    path('address/create', create_address, name='create_address'),
    path('address/<int:id>', address_detail, name='address_detail')
]
