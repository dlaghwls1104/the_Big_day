from django import forms
from map.models import Cafe

class CafeForm(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = ['name', 'kakaourl', 'pageurl']