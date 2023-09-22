from django import forms
from .models import Users


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'phone_number', 'people_number', 'date', 'time', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'data-rule': 'minlen:4', 'placeholder': 'Пожалуйста, укажите свое полное имя.',
                'data-msg': 'Please enter at least 4 chars'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Контактный номер', 'data-rule': 'minlen:4',
                'data-msg': 'Please enter at least 4 chars'
            }),
            'date': forms.TextInput(attrs={
                'class': 'form-control datepicker', 'placeholder': 'Выберите дату, на которое вы хотите забронировать '
                                                                   'стол', 'data-rule': 'minlen:4',
                'data-msg': 'Please enter at least 4 chars'
            }),
            'time': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Выберите время, на которое вы хотите забронировать стол',
                'data-rule': 'minlen:4',
                'data-msg': 'Please enter at least 4 chars'
            }),
            'people_number': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': "Сколько человек будет в вашей компании?",
                'data-rule': 'minlen:1',
                'data-msg': 'Please enter at least 1 chars'
            }),
            "comment": forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': "Пожалуйста, укажите любые дополнительные пожелания, чтобы мы "
                                                        "могли сделать ваш визит более комфортным. ",
                'data-rule': 'minlen:1', 'data-msg': 'Please enter at least 4 chars'
            })
        }
