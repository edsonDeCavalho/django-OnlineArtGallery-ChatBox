from django import forms
from .models import Profile


class FormControlProfile(forms.ModelForm):

    class Meta:
        model=Profile

        fields=[
        "name" ,
        "productID" ,
        "description" ,
        "img",
        "number"
        ]


