from django import forms
from .models import Post, UserPangolin
from django.contrib.auth.forms import UserCreationForm

class DatePickerInput(forms.DateInput):
        input_type = 'date'

class SignUpForm(UserCreationForm):
    my_date_field = forms.DateField(widget=DatePickerInput, label=("Birth date"))

    class Meta:
        model = UserPangolin
        fields = ('username', 'email','first_name' , 'last_name' ,'password1', 'password2','image','my_date_field')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'image',
        ]

class UserChangeForm2(forms.ModelForm):
    class Meta:
        model = UserPangolin
        fields = ('username', 'email','first_name', 'last_name','image')