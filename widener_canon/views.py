import json
import requests

from django.shortcuts import render
from django.http import HttpResponse
from IPython import embed
api_url = "http://api.lib.harvard.edu/v2/items.json?q="

def index(request):
    list_of_composers = get_list_of_composers()
    context = {'object_list': list_of_composers}
    return render(request, 'list_of_composers.html', context)

def get_list_of_composers():
    list_of_composers = []

    for i in range(600, 891):
        json_query = requests.get(api_url + 'Mus+{}.1.*&limit=1'.format(i))

        query_dict = json_query.json()

        if not query_dict['items']:
            response = "No composer is #1 for Mus {}!".format(i)
        else:
            try:
                composer = query_dict['items']['mods']['name'][0]['namePart'][0]
                if len(composer) < 2:
                    composer = "No composer "
            except KeyError:
                try:
                    composer = query_dict['items']['mods']['name']['namePart'][0]
                except:
                    response = "Check this record: {}".format(i)

            #location can have multiple entries
            #get last one (first one is not helpful)
            location_list = len(query_dict['items']['mods']['location'])

            try:
                location = query_dict['items']['mods']['location']['shelfLocator']
            except:
                location = query_dict['items']['mods']['location'][location_list-1]['shelfLocator']

            response = "{} is #1 for {}".format(composer, location[:9])
        list_of_composers.append(response)

    return list_of_composers
