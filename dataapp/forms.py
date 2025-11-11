from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ExcelData, Friend

class ExcelDataForm(forms.ModelForm):
    class Meta:
        model = ExcelData
        fields = ['column1', 'column2', 'column3', 'column4', 'column5', 'column6']
        widgets = {
            'column1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter value'}),
            'column2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter value'}),
            'column3': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'column4': forms.NumberInput(attrs={'class': 'form-control'}),
            'column5': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'column6': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'email', 'phone', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Friend name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1234567890'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Additional notes...'}),
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'