from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from ..models import User

User = get_user_model()

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = [User.USERNAME_FIELD] + User.REQUIRED_FIELDS + ['password1', 'password2']