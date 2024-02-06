from django import forms
from .models import User, Order

class SignUpForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    #def clean(self):
      #  cleaned_data = super().clean()
       # email = cleaned_data.get('email')
        #password = cleaned_data.get('password')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['county', 'address', 'phone']
       