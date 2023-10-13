from .models import Email
from django import forms


class EmailForm(forms.Form):
   email = forms.EmailField()
   subject = forms.CharField(max_length=1000)
   attach = forms.FileField(widget=forms.FileInput(attrs={'multiple':False}))
   message = forms.CharField(widget=forms.Textarea)

