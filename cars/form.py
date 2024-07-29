from django import forms
from cars.models import car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = car
        fields = '__all__'


    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 2000:
            self.add_error('value', 'Valor minimo do carro deve ser R$2.000,00')
        return value
    