from django import forms
from .models import Person

# person form
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'p-2 border border-gray-300 rounded-md mb-2 block w-full'}),
            'email': forms.EmailInput(attrs={'class': 'p-2 border border-gray-300 rounded-md mb-2 block w-full'}),
        }
