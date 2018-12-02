from django import forms
from .models import Order

# Code taken/adapted from lessons

class MakePaymentForm(forms.Form):
    
    MONTH_CHOICES = [(i,i) for i in range (1, 13)]
    YEAR_CHOICES = [(i, i) for i in range (2018, 2036)]
    
    credit_card_number = forms.CharField(label='Credit Card Number', required=False, widget=forms.TextInput(attrs={'placeholder': '**** **** **** ****', 'class':'ccclass'}))
    cvv = forms.CharField(label='Security code (CVV)', required=True, widget=forms.TextInput(attrs={'placeholder': '***'}))
    expiry_month = forms.ChoiceField(label='Expiry Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Expiry Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
    
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'address_line_1', 'address_line_2', 'town_or_city','county', 'country', 'postcode' )