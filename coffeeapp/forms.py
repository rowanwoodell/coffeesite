from django import forms
from .models import Coffee, Roaster, Country, TastingNote
from django_select2 import forms as s2forms

# class CoffeeForm(forms.Form):
#     name = forms.CharField(label="Coffee name", max_length=200)

class RoasterWidget(s2forms.Select2Widget):
    # queryset = Roaster.objects.all()

    search_fields = [
        "name__icontains",
    ]

    # attrs = {
    #     "data-maximum-selection-length": 1,
    #     "tags": True,
    # }

    # def value_from_datadict(self, data, files, name):
    #     values = super().value_from_datadict(data, files, name)
    #     pks = self.queryset.filter(**{'name__in': list(values)}).values_list('name', flat=True)
    #     pks = set(map(str, pks))
    #     cleaned_values = list(pks)
    #     for val in set(values) - pks:
    #         cleaned_values.append(self.queryset.create(name=val).pk)
    #     return cleaned_values

class CountryWidget(s2forms.Select2TagWidget):
    queryset = Country.objects.all()

    search_fields = [
        "name__icontains",
    ]

    def value_from_datadict(self, data, files, name):
        values = super().value_from_datadict(data, files, name)
        pks = self.queryset.filter(**{'name__in': list(values)}).values_list('name', flat=True)
        pks = set(map(str, pks))
        cleaned_values = list(pks)
        for val in set(values) - pks:
            cleaned_values.append(self.queryset.create(name=val).pk)
        return cleaned_values


class TastingNoteWidget(s2forms.Select2TagWidget):
    queryset = TastingNote.objects.all()

    search_fields = [
        "name__icontains",
    ]
    
    def value_from_datadict(self, data, files, name):
        values = super().value_from_datadict(data, files, name)
        pks = self.queryset.filter(**{'name__in': list(values)}).values_list('name', flat=True)
        pks = set(map(str, pks))
        cleaned_values = list(pks)
        for val in set(values) - pks:
            cleaned_values.append(self.queryset.create(name=val).pk)
        return cleaned_values

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