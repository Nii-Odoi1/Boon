from cProfile import label
from django import forms
from .models import Route

class RouterForm(forms.ModelForm):
    original_url = forms.CharField(widget=forms.TextInput(attrs={'class':'rounded-0'}), label="Original URL ")
    key = forms.CharField(widget=forms.TextInput(attrs={'class':'rounded-0'}), label="Shorten Key ")
    class Meta:
        model = Route
        fields = '__all__'
