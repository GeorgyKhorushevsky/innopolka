from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)
    phone_number = forms.IntegerField(required=True)

    class Meta:
        fields = [
            'username', 'first_name', 'last_name', 'email', 'address', 'phone_number',
        ]
        model = User


    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.address = self.cleaned_data['address']
        print(self.cleaned_data)
        user.phone_number = self.cleaned_data['phone_number']

        if commit:
            user.save(True)


class EditPatronForm(UserChangeForm):

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email'
        ]

