from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=50 ,widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Max of 150 characters. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class AddRecordForm(forms.ModelForm):

    first_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=50 ,widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Last Name'}))
    email = forms.CharField(label="", max_length=50 ,widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Email'}))
    phone = forms.CharField(label="", max_length=50 ,widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Phone'}))
    address = forms.CharField(label="", max_length=50 ,widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Address'}))
    city = forms.CharField(label="", max_length=50 ,widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'City'}))
    state = forms.CharField(label="", max_length=50 ,widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'State'}))
    zip_code = forms.CharField(label="", max_length=50 ,widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Zip Code'}))

    def __init__(self, *args, **kwargs):
        super(AddRecordForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["phone"].widget.attrs["class"] = "form-control"
        self.fields["address"].widget.attrs["class"] = "form-control"
        self.fields["city"].widget.attrs["class"] = "form-control"
        self.fields["state"].widget.attrs["class"] = "form-control"
        self.fields["zip_code"].widget.attrs["class"] = "form-control"


    class Meta:
        model = Record
        exclude = ("user",)