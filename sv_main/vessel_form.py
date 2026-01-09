from django import forms

class Item_form(forms.Form):
    item_form = forms.JSONField()