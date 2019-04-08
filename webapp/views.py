from django.shortcuts import render
import os
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http import HttpResponse
from webapp.models import user, SearchCriteria
from django.shortcuts import redirect
# Create your views here.
psqueue = []
xqueue = []
pcqueue = []
chat = []

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

def joinQueue(request):
    return

def search(queue):
    user1 = queue[0]
    foundUsers = []
    i = 1

    # Find potential matches
    while foundUsers.len() < 2 or i < 11:
        #Initializations
        newUser = queue[i] #Looking at the next user in the queue
        charBias = 0 #These are the various bias' based on the search criteria values
        locationBias = 0
        micBias1 = 0
        micBias2 = 0
        ageDiff = 0

        #Calculation of Bias'
        ageDiff = user1.criteria.age - newUser.age
        if ageDiff > 0: #Garuntees negative value for ageDiff
            ageDiff = 0 - ageDiff
        if user1.charactor == newUser.charactor:
            charBias = -10
        if user1.criteria.location == false and newUser.criteria.location == false:
            locationBias = 5 #Value if neither person cares about location
        elif user1.criteria.location == true and newUser.criteria.location == true:
            if user1.location == newUser.location: #Values if both people care about location
                locationBias = 20
            else:
                locationBias = -20
        elif user1.criteria.location == true or newUser.criteria.location == true:
            if user1.location == newUser.location: #Values if one or the other cares about location
                locationBias = 10
            else:
                locationBias = -10
        if user1.criteria.hasMic == true: #Values if user1 cares about mic usage
            if newUser.hasMic == true:
                micBias1 = 10
            elif newUser.hasMic == false:
                micBias2 = -10
        elif user1.criteria.hasMic == false:
            micBias1 = 5 #Value if user1 doesn't care about mic usage
        if newUser.criteria.hasMic == true: #Values if newUser cares about mic usage
            if user1.hasMic == true:
                micBias2 = 10
            elif user1.hasMic == false:
                micBias2 = -10
        elif newUser.criteria.hasMic == false:
            micBias1 = 5 #Value if newUser doesn't care about mic usage
        bias = ageDiff + charBias + locationBias + micBias1 + micBias2

        #Add user to potential matches if the bias is above a certain threshold.
        if bias >= 10:
            foundUser.append(newUser)
    return