from django.shortcuts import render
from customer.models import Customer
from .forms import CustomerForm
from enderecos.forms import EnderecoForm

def customers(request):


    query_set = Customer.objects.all()

    if 'phone' in request.GET:
        phone = request.GET['phone']
        if phone:
            query_set = Customer.objects.filter(phone_number=phone)

    context = {
        "customers": query_set,
    }

    return render(request, 'customers.html', context)

def create_customer(request):

    customerForm = CustomerForm()
    if request.method == "POST":
        customerForm = CustomerForm(request.POST)

    enderecoForm = EnderecoForm()
    if request.method == "POST":
        enderecoForm = EnderecoForm(request.POST)
        if enderecoForm.is_valid():
            enderecoForm.save()

    context = {
        "customerForm": customerForm,
        "enderecoForm": enderecoForm,
    }

    return render(request, 'createcustomer.html', context)

def details(request):
    return render(request, 'details.html', {})

def login(request):
    return render(request, 'login.html', {})

def equipe(request):
    return render(request, 'equipe.html', {})