from django import forms

NEWSLETTER_CHOICES = [
    ['all', 'I want it all'],
    ['important', 'I want only important'],
]

AGE_CHOICES = [
    [0, '0-18'],
    [19, '19-39'],
    [40, '40-59'],
    [60, '60+'],
]


class MyForm(forms.Form):
    email = forms.EmailField(max_length=1024)
    password = forms.CharField(max_length=1024, widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False)
    newsletter = forms.ChoiceField(
        choices=NEWSLETTER_CHOICES,
        widget=forms.RadioSelect,
    )
    age = forms.ChoiceField(choices=AGE_CHOICES)
    remarks = forms.CharField(required=False, widget=forms.Textarea)

    def clean_remarks(self):
        data = self.cleaned_data.get('remarks')
        if len(data) < 10:
            raise forms.ValidationError('Please enter at least 10 characters')
        return data