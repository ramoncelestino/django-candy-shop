from django import forms
from encomendas.models import Encomenda
from django.forms import DateTimeField

class EncomendaForm(forms.ModelForm):

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
        
        
