from django import forms
from .models import Contact

class SignupForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        } 
class LoginForm(forms.Form):
    name = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())
