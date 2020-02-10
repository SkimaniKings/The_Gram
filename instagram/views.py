
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
            return redirect("login")
        else:
                form=UserReagisterForm()
    return render(request, "index.html",{"form":form})

def login(request):
    
    
    return render(request, 'login.html',)

def profile(request):
    return render(request,'profile.html')


