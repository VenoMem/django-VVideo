import imp
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm 

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("video:video-list")
    else:
        form = UserRegistrationForm()
    return render(request, "user/register.html", {"form": form})


@login_required
def user(request):
    if request.method == "POST":
        updated_form = UserUpdateForm(request.POST, instance=request.user)
        if updated_form.is_valid():
            updated_form.save()
            return redirect("user")
    else:
        updated_form = UserUpdateForm(instance=request.user)

    return render(request, "user/user.html", {'updated_form':updated_form})