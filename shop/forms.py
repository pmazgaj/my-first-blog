"""
Used for editing forms (e.g. adding new Shop
"""
from django import forms
from .models import Shop


class ShopForm(forms.ModelForm):
    """
    Specifies what you're adding into Shop form.
    Don't use automatic fields.
    """

    class Meta:
        model = Shop
        fields = [
            "name",
            "description",
            "main_category",
            "categories",
            "shop_level",
            "is_in_lottery",
            "logo",

        ]
