from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from Accounts.forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from .models import Profile

from django.contrib.auth.models import User
# Create your views here.


def Register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, 'Account created successfully ! Please Login to Test')
            return redirect('/accounts/login')

    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def Profile(request):

    return render(request, 'accounts/profile.html')


def Profile_update(request):

    if request.method == 'POST':
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your Profile has been updated!')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)

    context = {'p_form': p_form, 'u_form': u_form}
    return render(request, 'accounts/profile_update.html', context)
