import json
import requests
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, 'services/home.html')


def all_services(request):
    service_path = request.get_full_path()
    response = requests.get(f'http://localhost:8001{service_path}')
    context = json.loads(response.content.decode('utf-8'))
    return render(request, 'services/services.html', context)


def order_service(request):
    return render(request, 'services/order.html')


def user_login(request):
    if request.method == 'GET':
        return render(request, 'services/user_login.html')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        response = requests.get(f'http://localhost:8001/login?email={email}&password={password}')

        context = {'status': response.status_code}

        if response.status_code == 200:
            context['services'] = json.loads(response.content.decode('utf-8'))
        return render(request, 'services/user_home.html', context)


def user_logout(request):
    pass
