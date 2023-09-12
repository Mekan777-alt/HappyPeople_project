from django import forms
from .models import Users


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'email', 'phone_number', 'people_number', 'date', 'time']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'data-rule': 'minlen:4', 'placeholder': 'Имя',
                'data-msg': 'Please enter at least 4 chars'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Ваш e-mail', 'data-rule': 'email',
                'data-msg': 'Please enter a valid email'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Контактный номер', 'data-rule': 'minlen:4',
                'data-msg': 'Please enter at least 4 chars'
            }),
            'date': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Дата', 'data-rule': 'minlen:4',
                'data-msg': 'Please enter at least 4 chars'
            }),
            'time': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Время', 'data-rule': 'minlen:4',
                'data-msg': 'Please enter at least 4 chars'
            }),
            'people_number': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Количество человек', 'data-rule': 'minlen:1',
                'data-msg': 'Please enter at least 1 chars'
            }),
        }