from django import forms
from .models import ExampleModel, OtherModel


class ExampleForm(forms.ModelForm):
    class Meta:
        model = ExampleModel
        # either "fields" or "exclude"
        fields = "__all__"


class OtherForm(forms.ModelForm):
    class Meta:
        model = OtherModel
        fields = "__all__"
