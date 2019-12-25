from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import RawVideo

class RawVideoForm(forms.ModelForm):
	class Meta:
		model = RawVideo
		fields = ['file']
		labels = {'file': ''}

class SearchForm(forms.Form):
    label = forms.CharField(max_length=30)
    begin_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)
    begin_time = forms.TimeField(required=False)
    end_time = forms.TimeField(required=False)
    camera = forms.IntegerField(required=False)

class UserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user