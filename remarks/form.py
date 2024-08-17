from django import forms
from .models import Remark

class RemarkForm(forms.ModelForm):
    class Meta:
        model = Remark
        fields = ['title', 'comments', 'rating']