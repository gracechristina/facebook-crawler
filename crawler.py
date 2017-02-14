import facebook
import requests
import json
import csv

def some_action(post):
    print(post['message'])

    #print (json.dumps(post),indent=4, sort_keys=True)


has_next_page = True

access_token = 'EAACEdEose0cBAJ3vq5rwwd5Xrb49WEnrMun3wHVgsnFgP4Igbk8jEDj3oZBEloPbbdFtTxujWSiY0c1UZAAwMZClqWv24YLraHbBxHYCXq7wxQegAZBxGG15AxsZBFLdFtfCfibG2ce6ZAt7rsdUUS3pM2x4L9ZCAZC30SCvhHBOcyXzkgdSjNKm3Ottav7ZBanoZD'

user = 'BillGates'
post_id = 'indonesiatravel'
graph = facebook.GraphAPI(access_token)
profile = graph.get_object(post_id)
posts = graph.get_connections(profile['id'], 'posts')
comments = graph.get_all_connections(profile['id'], 'comments')

while has_next_page:
    try:

        [some_action(post=post) for post in posts['data']]

        with open('data.txt', 'w') as outfile:
            json.dump(posts, outfile, sort_keys=True, indent=4)
       #request next page
        posts = requests.get(posts['paging']['next']).json()


    except KeyError:
        break