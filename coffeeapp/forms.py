from django import forms
from .models import Coffee, Country
from django_select2 import forms as s2forms

# class CoffeeForm(forms.Form):
#     name = forms.CharField(label="Coffee name", max_length=200)

class RoasterWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "name__icontains",
    ]

class CountryWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "country__icontains",
    ]

    # This doesn't seem to be functional at the moment
    # attrs = {
    #     "data-minimum-input-length": 0,
    #     "data-placeholder": "Select a country"
    # }

class TastingNoteWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "name__icontains",
    ]

class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ["name", "roaster", "roast_date", "origin", "roast_level", "tasting_notes"]
        widgets = {
            "roaster": RoasterWidget,
            "origin": CountryWidget,
            "tasting_notes": TastingNoteWidget,
        }

# class CoffeeForm(forms.Form):
#     origin_field = forms.ModelMultipleChoiceField(
#         widget = s2forms.ModelSelect2MultipleWidget(
#             model = Country,
#             search_fields = ["country__icontains"],
#             attrs = {
#                 "data-minimum-input-length": 0,
#                 "data-placeholder": "Select a country"
#             }
#         )
#     )