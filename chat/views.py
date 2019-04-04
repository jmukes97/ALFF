from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
import json
from webapp.models import user, SearchCriteria



def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    if not 'email' in request.session:
        return redirect("/")
    email = request.session['email']
    try:
        userObj = user.objects.get(pk=email)
    except user.DoesNotExist:
        return redirect("/")

    username = userObj.username
    return render(request, 'chat/room.html', {'room_name_json': mark_safe(json.dumps(room_name)), "user":username })
