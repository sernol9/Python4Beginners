from django import forms

class LoginForm (forms.Form):
    username = forms.CharField(max_length=1024)
    password = forms.CharField(max_length=1024, widget=forms.PasswordInput)

    def clean_username(self):
        data = self.cleaned_data.get('username')
        if data != 'admin':
            raise forms.ValidationError('Wrong username')
        return data

    def clean_password(self):
        data = self.cleaned_data.get('password')
        if data != 'password':
            raise forms.ValidationError('Wrong password')
        return data

