from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "class-name",
                "rows": 20,
                "columns": 120
            }
        )
    )
    price = forms.DecimalField(initial=0.00)

    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price"
        ]

    # def clean_<field_name>()
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "hmm" in title:
            raise forms.ValidationError("This is not a valid title")
        return title


class RawProductForm(forms.Form):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "class-name",
                "rows": 20,
                "columns": 120
            }
        )
    )
    price = forms.DecimalField(initial=0.00)
