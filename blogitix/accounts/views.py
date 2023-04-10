from django.contrib.auth import login# This line allows us to use the login() function to log in the user after they sign up
from django.shortcuts import render, redirect
from .forms import SignupForm # This line imports the SignupForm class from the forms.py file
from django.contrib import messages

def signup(request):
    error = ""
    if request.method == 'POST':
        form = SignupForm(request.POST) # This line creates a SignupForm object and passes the POST data to it
        if form.is_valid():
            user = form.save()
            login(request, user) # This line logs in the user after they sign up
            return redirect('profile') # Then redirect the user to the profile page after they sign up
        else:
            error = "Please correct the errors below."
    else:
        form = SignupForm() # This line creates a blank SignupForm object if the request is not a POST request
    return render(request, 'registration/signup.html', {'form': form, 'error': error})

def profile(request):
    return render(request, 'registration/profile.html')
