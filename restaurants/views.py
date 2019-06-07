from django.shortcuts import render

import requests
import json


def indexer(request):
    return render(request, 'restaurants/show_restaurants.html', {})


def restaurant_detail(request):

    api_key = 'esoKxYVxkGrRFTDcy9X3r9FxaBW1Zt8iUK3phPB6RnaYB4o2Iq8RzGShE0wVJQ053g-pI5658BZIP3kXogwHvn-2YHDiMODczKEfVz0FTzD_RNCuIoPJz58uca_2XHYx'
    headers = {'Authorization': 'Bearer %s' % api_key}

    #url = 'https://api.yelp.com/v3/businesses/search'
    url = 'https://api.yelp.com/v3/businesses/WavvLdfdP6g8aZTtbBQHTw'

    # In the dictionary, term can take values like food, cafes or businesses like McDonalds

    # params will probably be just location

    req = requests.get(url, headers=headers)

    # proceed only if the status code is 200
    # print('The status code is {}'.format(req.status_code))

    # printing the text from the response
    data = json.loads(req.text)

    # with open('data2.txt', 'w') as outfile:
    #json.dump(data, outfile)

    context = {
        'yelp_detail': data,
    }

    # Replace this with your real API key

    return render(request, 'restaurants/restaurant_detail.html', context)
