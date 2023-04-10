from django.contrib.auth.models import User # This line imports the User model from the built-in Django authentication system in order to pass it to the Meta class of the SignupForm class
from django.contrib.auth.forms import UserCreationForm # This line imports the UserCreationForm class from the built-in Django authentication system in order to create a custom user model
from django import forms # This line allows us to create a custom user model by extending the UserCreationForm class

class SignupForm(UserCreationForm):
    # This class is used to specify the model that the form is based on and the fields that the form will include
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    # This function is used to validate the email address entered by the user
    def clean_email(self): # self refer to the form object
        email = self.cleaned_data.get('email') # This line gets the email address entered by the user
        if User.objects.filter(email=email).exists(): # This line checks if the email address entered by the user already exists in the database
            raise forms.ValidationError("Email already exists")
        return email