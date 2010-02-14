from django import forms

class RegisterForm(forms.Form):
    email = forms.CharField(max_length=255, required=True, label="Email address")
    display_name = forms.CharField(max_length=255, required=True, label="Display Name")
    password = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput, label="Confirm Password")
