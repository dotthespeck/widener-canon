import json
import requests

api_url = "http://api.lib.harvard.edu/v2/items.json?q="

def get_list_of_composers():
    list_of_composers = []
    dict_of_call_nos = {}

    for i in range(600, 899):
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
                    if i in [610, 676, 694, 715, 821, 861, 870, 882, 885, 887]:
                        composer = query_dict['items']['mods']['name']['namePart']
                    else:
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
