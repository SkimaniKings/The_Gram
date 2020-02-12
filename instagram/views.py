
from django.shortcuts import render, redirect
from .forms import UserReagisterForm
from django.contrib import messages
from .models import Image

def home(request):
    form=UserReagisterForm()
    if request.method == "POST":
        form=UserReagisterForm(request.POST)
        if form.is_valid():
                
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, ("Account for {} has been created successfully").format(username))
            return redirect("login.html")
    else:
        form=UserReagisterForm()
    return render(request, "index.html",{"form":form})




def profile(request):
    return render(request,"profile.html")

def home_page(request):
    images = Image.objects.all()
    return render(request,"home.html",{"images":images})


