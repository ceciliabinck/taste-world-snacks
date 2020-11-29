from django import forms
from .widgets import CustomClearableFileInput
from .models import Product

# The different kind of forms


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
            label='image', required=False, widget=CustomClearableFileInput)
