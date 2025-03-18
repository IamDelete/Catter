from django import forms

class Signup_form(forms.Form):

    email = forms.EmailField()
    nume = forms.CharField(max_length=30)
    prenume = forms.CharField(max_length=30)
    coordonator_status= forms.BooleanField(required=False, initial=False)

class Login_form(forms.Form):
    email = forms.EmailField()
    parola = forms.CharField(widget=forms.PasswordInput)