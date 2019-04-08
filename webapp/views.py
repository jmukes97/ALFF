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
        email = request.session['email']
        userObj = user.objects.get(pk=email)
        boxInfo = ""
        if request.method == "POST":
            username = request.POST.get("c_user", "none")
            if not username == "none":
                userObj.username = username
            device = request.POST.get("c_device", "none")
            if not device == "none":
                userObj.device = device

            mic = request.POST.get("c_microphone", "none")
            if mic == "true":
                userObj.hasMic = True
            elif mic == "false":
                userObj.hasMic = False
            char = request.POST.get("c_char", "none")
            if not char == "none":
                userObj.charactor = char
            age = request.POST.get("c_age", "none")
            if not age == "none":
                userObj.age = age
            pmic = request.POST.get("p_microphone", "none")
            if pmic == "true":
                userObj.criteria.hasMic = True
            elif pmic == "false":
                userObj.criteria.hasMic = False
            pchar = request.POST.get("p_char", "none")
            if not pchar == "none":
                userObj.criteria.charactor = pchar 
                print(pchar)
        userObj.criteria.save()
        userObj.save() 
        return render(request, "profile.html", {"user": userObj, "info": boxInfo})
    return redirect("/")

def characters(request):
    status = "Log in / Sign up"
    return render(request, "characters.html", {"status": status})

def charactersLoggedIn(request):
    status = "Log Out"
    return render(request, "characters.html", {"status": status})

def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return redirect("/")
    else:
        return redirect("/")
