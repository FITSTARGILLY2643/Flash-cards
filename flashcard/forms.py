from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Folder, Card

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AddFolderForm(forms.ModelForm):
	class Meta:
		model = Folder
		fields = ('title',)

class AddCardForm(forms.ModelForm):
	class Meta:
		model = Card
		fields = ('title', 'notes')