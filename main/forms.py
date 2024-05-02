from django import forms
from .models import AddQuote, ContactList

# Create your forms here 
class AddQuoteForm(forms.ModelForm):
    class Meta:
        model = AddQuote
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Enter Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'example@gmail.com'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Phone Number'}),
            'service': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Service i.e assignment'}),
            'expected_time': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Expected Time i.e 24hrs'}),
            'details': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Details your request'}),
            'quote': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Quote i.e 5000'}),
        }

class ContactListForm(forms.ModelForm):
    class Meta:
        model = ContactList
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px; margin-bottom: 20px', 'placeholder': 'Enter Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'example@gmail.com'}),
            'message': forms.Textarea(attrs={'rows': 5,'style': 'width:100%'}), 
        }