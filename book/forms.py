from django import forms
from .models import Book, Comment

class CarForm(forms.ModelForm):
    class Meta: 
        model = Book
        # fields = '__all__'
        exclude = ['author','quantity']
        
class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name', 'email', 'body']

