from django import forms

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True, label="Email address")
    display_name = forms.CharField(max_length=255, required=True, label="Display Name")
    password = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput, label="Confirm Password")

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
