from django import forms
from .models import UserProfile

# The different kind of forms


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
        fields = '__all__'
