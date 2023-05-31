from django import forms
from .models import Categories


class Registration(forms.Form):
    name = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'name': 'name'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'name': 'age'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'name': 'email'}))


    options = [
        ('m', 'мужской'),
        ('j', 'женский')
    ]
    poll = forms.ChoiceField(choices=options, widget=forms.RadioSelect(attrs={'name': 'poll'}))
    password = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'name': 'password'}))

class Auth(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'name': 'email'}))
    password = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'name': 'password'}))

class AddNew(forms.Form):
    title = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'name': 'title'}))
    text = forms.CharField(min_length=5, widget=forms.Textarea(attrs={'name': 'text'}))
    categories = Categories.objects.all()
    cat = []
    for categorie in categories:
        cat.append((categorie.id, categorie.name))
    category = forms.ChoiceField(choices=cat, widget=forms.RadioSelect(attrs={'name': 'category'}))
    #image = forms.ImageField(widget=forms.FileInput(attrs={'name': 'img'}))