
from django import forms

class LoginForm(forms.Form):
    # Atributos del Formulario
    username = forms.CharField(widget=forms.TextInput() , required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)