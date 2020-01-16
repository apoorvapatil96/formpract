from django import forms
class RegistrationForm(forms.Form):
    first_name=forms.CharField(label="Enter your first name")
    last_name=forms.CharField(label="enter your last name")
    mobile=forms.IntegerField(label="Enter your mobile")
    email=forms.EmailField(label="Enter your email")
    username=forms.CharField(label='Enter your username')
    password1=forms.CharField(label='Enter your password')
    password2=forms.CharField(label='Confirm password')

class LoginForm(forms.Form):
    username=forms.CharField(label="Enter Username")
    password1=forms.CharField(label='Enter Password')