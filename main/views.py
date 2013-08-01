from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from main.forms import UserForm

def home(request):
    data = {}
    data['loop_times1'] = [i+1 for i in range(10)]
    data['loop_times2'] = [i+1 for i in range(10)]
    return render(request, 'main/home.html', data)

def login(request):
    import json
    data = {}
    if request.method == "POST":
        user = authenticate(username=request.POST["username"], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'success')
                form = UserForm(request.POST or None)
                data['username'] = form.username
                data['first_name'] = form.first_name
                data['last_name'] = form.last_name
                return HttpResponse(json.dumps(data), mimetype="application/json")
            else:
                messages.debug(request, 'Inactive User')
        else:
            messages.error(request, 'Invalid username')
    return render(request, "main/home.html", data)