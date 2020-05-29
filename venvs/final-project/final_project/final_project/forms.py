from django import forms

class MyForm(forms.Form):
    from_year = forms.IntegerField() 
    to_year = forms.IntegerField() 
    min_year, max_year = 0,0

    def min_max (self,*args):
        self.min_year = args[0]
        self.max_year = args[1]
        return

    def clean (self):
        data = self.cleaned_data
        year1 = data.get('from_year')
        year2 = data.get('to_year')
        if int(year1) > int(year2):
                raise forms.ValidationError(f"The 'From Year': {year1} field can't be larger than 'To Year'{year2} field")
        elif int(year1)<int(self.min_year) or int(year2)>int(self.max_year):
            raise forms.ValidationError(f"This is not a valid range. Enter values between {self.min_year} and {self.max_year}")
        return data