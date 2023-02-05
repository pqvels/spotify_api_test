import json
import requests
from secrets import spotify_token, spotify_user_id


idlist = []
query = "https://api.spotify.com/v1/me/following?type=artist"
response = requests.get(query, headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(spotify_token)})
response_json = response.json()
#print(response.text)
for i in response_json["artists"]["items"]:
    idlist.append(i["id"])
#    print((i["id"]))
#print(idlist[-1])

def get_artists_id():
    after_id = idlist[-1]
    query2 = "https://api.spotify.com/v1/me/following?type=artist&after={}&limit=50".format(after_id)
    response2 = requests.get(query2, headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(spotify_token)})
    response2_json = response2.json()
    for i in response2_json["artists"]["items"]:
        idlist.append(i["id"])
    print(after_id)
get_artists_id()
get_artists_id()
print(idlist)
print(len(idlist))
