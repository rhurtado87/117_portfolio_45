from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'placeholder': ' Your Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Message'}))
