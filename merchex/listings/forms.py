from django import forms


class ContactUsForm(forms.Form):
    # required=False présise que le champ est facultatif
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)
