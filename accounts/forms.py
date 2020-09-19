from django import forms

from .models import Account


class LoginForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        fieldsMap = {
            "email": "ایمیل",
            "password": "پسورد"
        }
        # Assigning class and placeholder and removeing label from fields
        for k, v in self.fields.items():
            self.fields[k].label = ""
            v.widget.attrs['class'] = 'input'
            if k in fieldsMap:
                v.widget.attrs['placeholder'] = fieldsMap[k]

    class Meta:
        model = Account
        fields = ["email", "password"]


class RegistrationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        fieldsMap = {
            "first_name": "نام",
            "last_name": "خانوادگی",
            "username": "نام کاربری",
            "email": "ایمیل",
            "password": "پسورد"
        }
        # Assigning class and placeholder and removeing label from fields
        for k, v in self.fields.items():
            self.fields[k].label = ""
            v.widget.attrs['class'] = 'input'
            if k in fieldsMap:
                v.widget.attrs['placeholder'] = fieldsMap[k]

    class Meta:
        model = Account
        fields = ["first_name", "last_name", "username", "email", "password"]
