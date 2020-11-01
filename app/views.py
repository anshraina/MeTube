from django.shortcuts import render, HttpResponse, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import VideoForm
from .models import Video


def index(request):
    all_video = Video.objects.all()
    if request.method == "POST":
        form = VideoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Uploaded successfully </h1>")
    else:
        form = VideoForm()
    return render(request, 'index.html', {"form": form, "all": all_video})


def registration(request):
    if request.method == "POST":
            user_form = RegistrationForm(request.POST)
            if user_form.is_valid():
                user_form.save()
                print("Hey1")
                return HttpResponse("<h1> Registration successful</h1>")
            else:
                print("Hii")
                return HttpResponse("<h1> Registration unsuccessful</h1>")

    else:
        print("Hey")
        user_form = RegistrationForm()
        return render(request, 'registration.html', {'user_form': user_form})


# ------- Login Form --------
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd["username"], password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("home")
                else:
                    return HttpResponse("<h1> Disable Account </h1>")
            else:
                return HttpResponse("Invalid Login")
    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form})


@login_required
def user_logout(request):
    logout(request)
    return redirect("home")

