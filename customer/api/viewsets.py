from rest_framework.viewsets import ModelViewSet
from customer.models import Customer
from .serializers import CustomerSerializer


class CustomerViewset(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer