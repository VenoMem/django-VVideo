import imp
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm 

def register(request):
    if request == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = user.cleaned_data.get('username')
            messages.success(request, f"New Account: {username}")
            login(request, user)
            messages.info(request, f"Logged In as: {username}")
            return redirect("video:video-list")
    else:
        form = UserRegistrationForm()
    return render(request, "user/register.html", {"form":form})


@login_required
def profile(request):
    if request.method == "POST":
        updated_form = UserUpdateForm(request.POST, instance=request.user)
        if updated_form.is_valid():
            updated_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("user")
    else:
        updated_form = UserUpdateForm(instance=request.user)

    return render(request, "user/user.html", {'updated_form': updated_form})