from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def blank(request):
    return redirect('Home')

def home(request):
    return render(request, 'App/home.html')

def actions(request):
    actions = Actions.objects.all()[:4]
    return render(request, 'App/actions.html', {'actions': actions})

def action(request, action_id):
    action = Actions.objects.get(id=action_id)
    return render(request, 'App/action_details.html', {'action': action, 'current_url': request.build_absolute_uri()})

def perform(request, action_id):
    action = Actions.objects.get(id=action_id)
    return render(request, 'App/perform_actions.html', {'action': action})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        ContactUs.objects.create(name=name, email=email, message=message)
        return redirect('Home')
    return render(request, 'App/contact_us.html')

def contact_messages(request):
    if request.user.is_authenticated:
        all_messages = ContactUs.objects.all()
        count = all_messages.count()
        return render(request, 'App/contact_us_messages.html', {'all_messages': all_messages, 'count': count})
    else:
        messages.error(request, 'You are not authorized to view messages.')
        return render(request, 'App/contact_us_messages.html')

def team(request):
    return render(request, 'App/team.html')

def login(request):
    return redirect('/admin/')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('Home')
