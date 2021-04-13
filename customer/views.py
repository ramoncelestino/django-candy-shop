from django.shortcuts import render, redirect
from customer.models import Customer
from .forms import CustomerForm
from enderecos.forms import EnderecoForm
 

def customers(request):


    query_set = Customer.objects.all()

    if 'phone' in request.GET:
        phone = request.GET['phone']
        if phone:
            query_set = Customer.objects.filter(phone_number=phone)

    if 'nome' in request.GET:
        nome = request.GET['nome']
        if nome:
            query_set= Customer.objects.filter(name__icontains=nome)

    context = {
        "customers": query_set,
    }

    return render(request, 'customers.html', context)

def create_customer(request):

    customerForm = CustomerForm()
    if request.method == "POST":
        customerForm = CustomerForm(request.POST or None)
        if customerForm.is_valid:
            customerForm.save()
            customerForm = CustomerForm()
            return redirect(customers)

    enderecoForm = EnderecoForm()

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

def main(request):
    return render(request, 'index.html', {})