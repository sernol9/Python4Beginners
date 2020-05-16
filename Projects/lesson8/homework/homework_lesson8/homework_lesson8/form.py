from django import forms

class LoginForm (forms.Form):
    username = forms.CharField(max_length=1024)
    password = forms.CharField(max_length=1024, widget=forms.PasswordInput)

    def clean_username(self):
        data = self.cleaned_data.get('username')
        # do your custom validation code here
        # if you found an error, you can do this:
        # raise forms.ValidationError("Error message")
        return data

    def clean_password(self):
        data = self.cleaned_data.get('password')
        # do your custom validation code here
        # if you found an error, you can do this:
        # raise forms.ValidationError("Error message")
        return data

