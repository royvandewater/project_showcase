from django import forms

from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=255, required=True, label="Username")
    first_name = forms.CharField(max_length=255, required=True, label="First Name")
    last_name = forms.CharField(max_length=255, required=True, label="Last Name")
    email = forms.EmailField(required=True, label="Email address")
    password = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput, label="Confirm Password")

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).count() == 0:
            return username
        raise forms.ValidationError("That username is already taken")

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).count() == 0:
            return email
        raise forms.ValidationError("An account with that email address already exists")

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) > 5:
            return password
        raise forms.ValidationError("Password must be at least 6 characters")

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            if password != confirm_password:
                raise forms.ValidationError("Passwords do not match")
        return confirm_password

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True, label="Username")
    password = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput, label="Password")

class ResetForm(forms.Form):
    email = forms.EmailField(required=True, label="Email address")

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).count() > 0:
            return email
        raise forms.ValidationError("There does not exist an account with that email address")
