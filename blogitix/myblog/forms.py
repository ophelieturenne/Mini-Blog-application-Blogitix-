from django import forms # This line imports the forms from django in order to create a form.
from .models import Post


class PostForm(forms.ModelForm):
    # Meta class is used to define the properties of the form.
    class Meta:
        model = Post # This line defines the model that will be used to create the form.
        fields = ('title', 'slug', 'author', 'category', 'content') # This line defines the fields that will be displayed in the form.
        widgets = { # This line defines the type of widget to be used for each field.
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title'}), # TextInput is a widget that allows the user to enter text.
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a slug'}), # Slug is a short label for something, containing only letters, numbers, underscores or hyphens.
            'category': forms.Select(attrs={'class': 'form-control'}), # Select is a widget that allows the user to select a value from a list.
            'author': forms.HiddenInput(), # Hide the author field
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a text'})
        }

class UpdatePostForm(forms.ModelForm):
    # Meta class is used to define the properties of the form.
    class Meta:
        model = Post # This line defines the model that will be used to create the form.
        fields = ('title', 'category', 'content') # This line defines the fields that will be displayed in the form.
        widgets = { # This line defines the type of widget to be used for each field.
            'title': forms.TextInput(attrs={'class': 'form-control mt-2 text-secondary', 'placeholder': 'Enter a title'}), # TextInput is a widget that allows the user to enter text.
            'category': forms.Select(attrs={'class': 'form-control mt-2 text-secondary'}), # Select is a widget that allows the user to select a value from a list.
            'content': forms.Textarea(attrs={'class': 'form-control mt-2 text-secondary', 'placeholder': 'Enter a text'})
        }
