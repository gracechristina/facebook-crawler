import facebook
import requests
import json
import csv
import urllib.request
import time

def request_until_succeed(url):
    req = urllib.request.Request(url)
    success = False
    while success is False:
        try:
            response = urllib.request.urlopen(req)
            if response.getcode() == 200:
                success = True
        except Exception as e:
            print(e)
            time.sleep(5)

            print("Error for URL %s: %s" % (url, datetime.datetime.now()))
            print("Retrying.")

    return response.read().decode(response.headers.get_content_charset())




def some_action(post):
    print(post['message'])

    #print (json.dumps(post),indent=4, sort_keys=True)


has_next_page = True

access_token = 'EAACEdEose0cBACxe2nRKAym8jKReDWHZBBTf8IZCBQZAS9ZBtsxc5UZAXCJobPZAsHsndvRt2IXSFClLZANgTpbl0XQDjdEDnl32OLzUjclVEhpoQlsbeWJktEZCZAE3Go0kti4mLHIIWSP686oH3sj0XjKNUdDDgwS1EY34kh2PkoPJ03282JcJQchyZC4ZB7KCNYZD'

user = 'BillGates'
post_id = 'indonesiatravel'
graph = facebook.GraphAPI(access_token)
profile = graph.get_object(post_id)
posts = graph.get_connections(profile['id'], 'posts')
comments = graph.get_all_connections(profile['id'], 'comments')

base = "https://graph.facebook.com/v2.8"
node = "/%s/posts" % post_id
fields = "/?fields=message,link,created_time,type,name,id," + \
            "comments.limit(0).summary(true),shares,reactions" + \
            ".limit(0).summary(true)"
parameters = "&limit=%s&access_token=%s" % (100, access_token)
url = base + node + fields + parameters

while has_next_page:
    try:

        [some_action(post=post) for post in posts['data']]

        with open('data.json', 'w') as outfile:
             json.dump(posts, outfile, sort_keys=True, indent=4)
       #request next page
         #posts = requests.get(posts['paging']['next']).json()
        posts = json.loads(request_until_succeed(url))

    except KeyError:
        break