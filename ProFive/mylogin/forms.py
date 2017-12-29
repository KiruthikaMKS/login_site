from django import forms
from mylogin.models import UserProfile,User

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'someone@example.com'}))
    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('portfolio','profilePic')
