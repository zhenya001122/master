from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    age = forms.IntegerField(min_value=18, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, label="Email")
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())