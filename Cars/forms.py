from django import forms
from .models import Car_details
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CarForm(forms.ModelForm):
    class Meta:
        model = Car_details
        fields = ['car_Name','content', 'Car_Model','car_Price','car_photo']

class SignUpForm(UserCreationForm):
      email = forms.EmailField(required=True, help_text='Required. Provide a valid email address.')

      class Meta:
          model = User
          fields = ['username', 'email', 'password1', 'password2']