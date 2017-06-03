from django import forms

class StockForm(forms.Form):
    codeid = forms.DecimalField(max_value=9999, min_value=0000, max_digits=4,widget=forms.TextInput(attrs={'class': 'form-control','name':'codeid','value':'1101'}))
    startdate = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','name':'startdate','type':'date','value':'2016-05-25'}))
    enddate = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','name':'enddate','type':'date','value':'2017-05-25'}))
