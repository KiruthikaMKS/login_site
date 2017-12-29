from django.shortcuts import render
from mylogin.forms import UserForm,UserProfileForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.

@login_required
def user_logout(req):
    logout(req)
    return HttpResponseRedirect(reverse('welcome'))

def welcome(req):
    return render(req,'welcome.html')

def register(req):
    registered = False

    if req.method == 'POST':
        user_form = UserForm(req.POST)
        profile_form = UserProfileForm(req.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.users = user

            if 'profilePic' in req.FILES:
                profile.profilePic = req.FILES['profilePic']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm
        profile_form = UserProfileForm
    return render(req,'register.html',
                      {'user_form':user_form,
                       'profile_form':profile_form,
                       'registered':registered})

def user_login(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        pwd = req.POST.get('password')

        user = authenticate(username=username,password=pwd)

        if user:
            if user.is_active:
                login(req,user)
                return HttpResponseRedirect(reverse('welcome'))
            else:
                return HttpResponse("acc not active")
        else:
            return HttpResponse("account invalid")
    else:
        return render(req,'login.html',{})
