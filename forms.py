from django import forms
from django.forms import ModelForm
from snpt.models import Snippet

class SnippetForm(ModelForm):
    code = forms.CharField(widget=forms.Textarea(attrs={'rows':20, 'cols': 100}))
    class Meta:
        model = Snippet
        fields = ('code','lexer','caption','author','url','email')
