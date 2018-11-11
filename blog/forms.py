from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=60)
    last_name = forms.CharField(label='Last name', max_length=60)
    email = forms.EmailField()
    question = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField()    
    comment = forms.CharField(widget=forms.Textarea)