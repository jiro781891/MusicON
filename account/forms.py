from django import forms
from django.contrib.auth.models import User



class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput)
    password2 = forms.CharField(widget= forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username', 'email']

    #Validatin password

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise ValidationError("Password don't match")

        return cd['password2']
