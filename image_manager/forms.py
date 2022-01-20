
from django import forms
from .models import Image, Description


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['image']

class DescriptionForm(forms.ModelForm):

    class Meta:
        model = Description
        fields = ['description', 'image']
