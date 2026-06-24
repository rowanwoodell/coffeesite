from django import forms
from .models import Coffee

# class CoffeeForm(forms.Form):
#     name = forms.CharField(label="Coffee name", max_length=200)

class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ["name", "roaster", "roast_date", "origin", "roast_level", "tasting_notes"]