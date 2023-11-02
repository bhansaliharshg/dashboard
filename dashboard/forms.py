from django import forms

class SearchForm(forms.Form):
    state = forms.ChoiceField(label='State', required=True)
    district = forms.ChoiceField(label='District', required=False)
    block = forms.ChoiceField(label='Block', required=False)
    fromDate = forms.DateField(required=False)
    toDate = forms.DateField(required=False)