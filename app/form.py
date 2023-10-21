from django import forms


class MyForm(forms.Form):
    name = forms.CharField(label="Name")
    email = forms.EmailField(label="Email")
    age = forms.IntegerField(label="Age")
