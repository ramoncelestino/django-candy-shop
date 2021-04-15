from django import forms
from encomendas.models import Encomenda
from django.forms import DateTimeField
from django.forms import ModelChoiceField
from customer.models import Customer

class EncomendaForm(forms.ModelForm):


    cliente = ModelChoiceField(queryset=Customer.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    data_encomenda = DateTimeField(input_formats=["%d/%m/%Y"], widget=forms.DateTimeInput(format="%m/%d/%Y", attrs={
                                'class': 'form-control datetimepicker-input',
                                'data-target': '#datetimepicker1'
                            }))
    data_entrega = DateTimeField(input_formats=["%d/%m/%Y"], widget=forms.DateTimeInput(format="%m/%d/%Y", attrs={
                                'class': 'form-control datetimepicker-input',
                                'data-target': '#datetimepicker1'
                            }))

    class Meta:
        model = Encomenda
        fields = '__all__'
        
        
