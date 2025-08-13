from django import forms


class UrlForm(forms.Form):
    url = forms.URLField(
        label="URL",
        widget=forms.URLInput(attrs={'placeholder': 'https://www.example.com'})
    )
