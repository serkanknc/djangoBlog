from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate, logout
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password= password)
        if user is None:
            messages.info(request,"Kullanıcı adı veya şifre hatalı",extra_tags="danger")
            return render(request,'login.html',context)
        messages.success(request,"Giriş Başarılı")
        login(request,user)
        return redirect('index')
    return render(request,'login.html',context)

def registerUser(request):

    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")

        
        if User.objects.filter(username=username).exists():
            messages.info(request,"Kullanıcı adı sistemde zaten kayıtlı",extra_tags="warning")
            return render(request,'register.html',context)

        user = User.objects.create_user(username = username,email = email,password=password)
        login(request,user)
        messages.success(request,"Başarıyla kayıt oldunuz")
        return redirect('index')
    
    return render(request,'register.html',context)



def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yapıldı")
    return redirect('index')
