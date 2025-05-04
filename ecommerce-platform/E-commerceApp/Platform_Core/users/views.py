from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import CustomUserCreationForm,  ProfileUpdateForm, CustomPasswordChangeForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # or redirect to 'product-list'
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)

        if profile_form.is_valid() and password_form.is_valid():
            profile_form.save()
            password_form.save()
            update_session_auth_hash(request, password_form.user)  # keep user logged in
            messages.success(request, 'Your profile and password were updated successfully.')
            return redirect('profile')  # or any success page
    else:
        profile_form = ProfileUpdateForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'users/profile.html', {
        'profile_form': profile_form,
        'password_form': password_form
    })