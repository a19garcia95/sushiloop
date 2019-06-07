from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from accounts.views import *

# Create your views here.


def index(request):
    return render(request, 'pages/index.html', {})


def about(request):
    return render(request, 'pages/about.html', {})


def search_results(request):

    if request.method == 'POST':
        search = request.POST['search_results']
        print(search)

        api_key = 'esoKxYVxkGrRFTDcy9X3r9FxaBW1Zt8iUK3phPB6RnaYB4o2Iq8RzGShE0wVJQ053g-pI5658BZIP3kXogwHvn-2YHDiMODczKEfVz0FTzD_RNCuIoPJz58uca_2XHYx'
        headers = {'Authorization': 'Bearer %s' % api_key}

        url = 'https://api.yelp.com/v3/businesses/search'

        params = {'term': 'restaurants', 'categories': 'japanese,all', 'location': search,
                  'price': '4', 'limit': 9, 'sort_by': 'review_count'}

        req = requests.get(url, params=params, headers=headers)

        data = json.loads(req.text)

        context = {
            'search': search,
            'data': data,
        }

    return render(request, 'pages/search_results.html', context)
