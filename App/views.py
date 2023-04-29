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
    actions = Actions.objects.all().order_by('action_order')[:4]
    return render(request, 'App/actions.html', {'actions': actions})

def action(request, action_id):
    action = Actions.objects.get(id=action_id)
    return render(request, 'App/action_details.html', {'action': action, 'current_url': request.build_absolute_uri()})

def perform(request, action_id):
    action = Actions.objects.get(id=action_id)
    steps = ActionSteps.objects.get(action=action)
    print(steps.step1)
    action.times_performed += 1
    action.save()
    return render(request, 'App/action.html', {'action': action, 'steps': steps})

def perform_log(request):
    actions = Actions.objects.all()
    count=0
    for action in actions:
        count+=action.times_performed
    return render(request, 'App/perform_logs.html', {'actions': actions, 'count': count})

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
