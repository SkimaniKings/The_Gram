
from django.shortcuts import render, redirect
from .forms import UserReagisterForm
from django.contrib import messages

def home(request):
    form=UserReagisterForm()
    if request.method == "POST":
        form=UserReagisterForm(request.POST)
        if form.is_valid:
                
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f("Account for {username} has been created successfully"))
            return redirect("login.html")
        else:
                form=UserReagisterForm()
    return render(request, "home.html",{"form":form})


