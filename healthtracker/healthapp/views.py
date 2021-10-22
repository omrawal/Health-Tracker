from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .forms import StatisticCreate
from .models import Statistic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.
# SUPERUSER credentails
# username = admin
# password = admin143


def index(request):
    return render(request, 'index.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {'form': AuthenticationForm()}
        return render(request, 'login.html', context)
    return render(request, 'login.html')


@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return render(request, 'logout.html')


def registerPage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)


@login_required(login_url='login')
def progressPage(request):
    context = {}
    return render(request, 'progress.html', context)


@login_required(login_url='login')
def addStatsPage(request):
    upload = StatisticCreate()
    if request.method == 'POST':
        upload = StatisticCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'addstats.html', {'upload_form': upload})
