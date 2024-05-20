
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .form import SignupForm, LoginForm
from django.http import HttpResponse
from .form import SignupForm
from loginsystem.sentence_imp import improve_sentence
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



def index(request):
    return render(request, 'index.html')


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful signup
            return redirect('login')  # Change this to wherever you want to redirect after signup
        else:
            return HttpResponse("Form is not valid. Please ensure all fields are correctly filled.")
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('dashboards')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    logout(request)
    return redirect('home')

def dashboards(request):
    return render(request ,'dashboards.html')



def sentence_importance(request):
    if request.method == 'POST':
        sentence = request.POST.get('sentence', '')
        improved_sentence = improve_sentence(sentence)
        return render(request, 'sentence_importance.html', {
            'original_sentence': sentence,
            'improved_sentence': improved_sentence
        })
    return render(request, 'sentence_importance.html')