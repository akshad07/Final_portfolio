from django import forms
from django.contrib.auth.forms import User



STATUS=(
    (0,"Draft"),
    (1,"Publish")
)

class BlogForm(forms.Form):
    title = forms.CharField(max_length=200)
    category = forms.SlugField(max_length=200)
    content = forms.CharField()
    status = forms.IntegerField(widget=forms.Select(choices=STATUS))
   


    
