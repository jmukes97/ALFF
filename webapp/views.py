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
seed = 1000000

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
            state = request.POST.get("state", "NA")
            if not state == "NA":
                userObj.location = state
            username = request.POST.get("c_user", "none")
            print(username)
            if not username == "none":
                if username:
                    userObj.username = username
                else:
                    pass
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
            print(age)
            if not age == "none":
                if age:
                    userObj.age = age
                else:
                    pass
            pmic = request.POST.get("p_microphone", "none")
            if pmic == "true":
                userObj.criteria.hasMic = True
            elif pmic == "false":
                userObj.criteria.hasMic = False
            pchar = request.POST.get("p_char", "notSelected")
            if not pchar == "notSelected":
                userObj.criteria.charactor = pchar 
                print(pchar)
            locPref = request.POST.get("p_loc", "none")
            if not locPref == "none":
                if locPref == "true":
                    userObj.criteria.location = True
                else:
                    userObj.criteria.location = False
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

def joinQueue(request):
    return

def search(queue):
    if queue.len() < 3:
        return
    user1 = queue[0]
    foundUsers = []
    foundUsersBias = []
    i = 1

    # Find potential matches
    while len(foundUsers) < 2 or i < 11:
        #Initializations
        newUser = queue[i] #Looking at the next user in the queue
        charBias = 0 #These are the various bias' based on the search criteria values
        locationBias = 0
        micBias1 = 0
        micBias2 = 0
        ageDiff = 0
        i += 1

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
            foundUsers.append(newUser)
            foundUsersBias.append(bias)

    #Find the final matches from the list of potential matches
    finalMatches = []
    if foundUsers.len() == 2:
        finalMatches = foundUsers
    while finalMatches.len() < 2:
        max = 0
        maxInd = -1
        for i in foundUsersBias:
            if foundUsersBias[i] > max:
                max = foundUsersBias[i]
                maxInd = i
        finalMatches.append[foundUsers[maxInd]]
        foundUsersBias[maxInd] = 0

    #Add the found users to the chat wrapped in a chat object
    chat.append(Chat(user1, finalMatches[0], finalMatches[1], seed))
    seed = seed + 1
    return

#Class for encapsulating the users and chat seed
class Chat:
    def __init__(self, user1, user2, user3, seed):
        self.user1 = user1
        self.user2 = user2
        self.user3 = user3
        self.seed = seed
