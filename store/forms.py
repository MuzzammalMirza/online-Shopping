from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    password1 = forms.CharField(label ='Confirm Password',widget = forms.PasswordInput(attrs = {'class':'form-control','placeholder':'Enter your password'}))
    password2 = forms.CharField(label = 'Confirm Password Again',widget= forms.PasswordInput(attrs = {'class':'form-control','placeholder':'Enter your password Again'}))
    class Meta:
        model = User
        fields = ['username','email']
        label = {'email':'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your username without space'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter your Email '})}


class loginForm(AuthenticationForm):

    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=('password'), widget=forms.PasswordInput(attrs={'autofocus': True, 'autocomplete': 'current-password', 'class': 'form-control'}))
#
# class Postform(forms.ModelForm):
#     class Meta:
#         model = Post
#
#         fields=['titel','des']
#         labels = {'titel':'Titel','des':'Descrtiption'}
#         widgets = {'titel':forms.TextInput(attrs={'class':'form-control'}),
#         'des':forms.Textarea(attrs={'class':'form-control'})}

