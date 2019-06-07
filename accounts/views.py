from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from pages import *

import requests
import json


def main(request):

    return redirect('/')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                print('there is already a user with that username')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    print('email already being used')
                    return redirect('register')
                else:
                    # looks good
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # login after register
                    # auth.login(request, user)
                    # return redirect('')
                    user.save()
                    print('you are now registered and can log in')
                    return redirect('login')
        else:
            print("passwords dont match")
    else:
        return render(request, 'accounts/register.html', {})


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('you are now logged in')
            return redirect('main')
        else:
            print('invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html', {})


def logout(request):

    if request.method == 'POST':
        auth.logout(request)
        print('you are now logged out')
        return redirect('main')

    return redirect('index')


def testing_api(request):

    # post request, variable = location

    api_key = 'esoKxYVxkGrRFTDcy9X3r9FxaBW1Zt8iUK3phPB6RnaYB4o2Iq8RzGShE0wVJQ053g-pI5658BZIP3kXogwHvn-2YHDiMODczKEfVz0FTzD_RNCuIoPJz58uca_2XHYx'
    headers = {'Authorization': 'Bearer %s' % api_key}

    url = 'https://api.yelp.com/v3/businesses/search'

    # In the dictionary, term can take values like food, cafes or businesses like McDonalds
    params = {'term': 'sushi', 'location': 'New York',
              'price': '2', 'limit': 6}

    # params will probably be just location

    req = requests.get(url, params=params, headers=headers)

    # proceed only if the status code is 200
    # print('The status code is {}'.format(req.status_code))

    # printing the text from the response
    data = json.loads(req.text)

    # with open('data2.txt', 'w') as outfile:
    # json.dump(data, outfile)
    context = {
        'yelp_results': data,
    }

    return render(request, 'accounts/testing_api.html', context)
