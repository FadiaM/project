from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import MyClubUser


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput())
    password = forms.CharField(label='Confirm password', max_length=32, widget=forms.PasswordInput())

    class Meta:
        model = MyClubUser
        fields = ('email',)
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput()
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = MyClubUser.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        super().__init__()
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'placeholder': '',
            })
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'placeholder': '',
            })


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyClubUser
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyClubUser
        fields = ('email', 'password', 'active', 'admin')

    def clean_password(self):
        return self.initial["password"]
