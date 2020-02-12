
from django.shortcuts import render, redirect
from .forms import UserReagisterForm,UserUpdateForm,ProfileUpdateForm,PostUpdateForm
from django.contrib import messages
from .models import Image,Profile,Post
from django.contrib.auth.decorators import login_required

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



@login_required()
def profile(request):
    posts = Post.objects.all()
    
    return render(request,"profile.html",{"posts":posts})

def home_page(request):
    posts = Post.objects.all()
    images = Image.objects.all()
    return render(request,"home.html",{"images":images,"posts": posts})

@login_required()
def update(request):
  if request.method == "POST":
    u_form = UserUpdateForm(request.POST)
    p_form = ProfileUpdateForm(request.POST, request.FILES)
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
    #   p_form.save()
      messages.success(request, "Profile updated successfully")
      return redirect("update")
  else:
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm()
  context = {
    "u_form" : u_form,
    "p_form" : p_form
  }
  return render(request, "update_profile.html", context)

@login_required()
def post_image(request):
    
    if request.method == "POST":
        form=PostUpdateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home_page")
    else:
        form=PostUpdateForm
  
    return render(request,"post_image.html",{"form":form})




