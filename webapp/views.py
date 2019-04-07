from django.shortcuts import render
import os
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http import HttpResponse
from webapp.models import user, SearchCriteria
from django.shortcuts import redirect
# Create your views here.

def index(request):
    return render(request, "index.html")
def login(request):
    if 'email' in request.session:
        return redirect("/profile/")
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            userObj = user.objects.get(pk=email)
        except user.DoesNotExist:
            return render(request, "loginError.html")
        if userObj.password == password:
            request.session['username'] = userObj.username
            request.session['age'] = userObj.age
            request.session['email'] = userObj.email
            return redirect("/profile/")
        else:
            return render(request, "loginError.html")
    return render(request, "login.html")
def signup(request):
    if request.method == "POST":
        newEmail = request.POST['email']
        try:
            userObj = user.objects.get(pk=newEmail)
        except user.DoesNotExist:
            newPassword = request.POST['psw']
            newEmptyCriteria = SearchCriteria()
            newEmptyCriteria.save()
            newUsername = request.POST['uname']
            newAge = request.POST['age']
            newUser = user(email=newEmail, username=newUsername, password=newPassword, age=newAge, criteria = newEmptyCriteria)
            newUser.save()
            return render(request, "signupSucc.html")
        return render(request, "signupFail.html")
    return render(request, "signup.html")

def profile(request):
    if 'email' in request.session:
        print(request.session['email'])
        return render(request, "profile.html", {"username": request.session['username'], "email": request.session['email'], "age": request.session['email']})
    return redirect("/")

def characters(request):
    return render(request, "characters.html")

def charactersLoggedIn(request):
    return render(request, "charactersLoggedIn.html")

def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return redirect("/")
    else:
        return redirect("/")