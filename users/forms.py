from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Custom user registration form extending Django's UserCreationForm
class UserRegisterForm(UserCreationForm):
    # Adding an email field to the form
    email = forms.EmailField()

    class Meta:
        model = User
        # Specifying the fields to include in the form
        fields = ['username', 'email', 'password1', 'password2']

# Custom user update form for updating user details
class UserUpdateForm(forms.ModelForm):
    # Adding an email field to the form
    email = forms.EmailField()

    class Meta:
        model = User
        # Specifying the fields to include in the form
        fields = ['username', 'email']

# Custom form for updating the user's profile image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        # Specifying the fields to include in the form
        fields = ['image']
