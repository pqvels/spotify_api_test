import json
import requests
from secrets import spotify_token, spotify_user_id




ids1 =  "31jvzuB4ikftPQZJwrYfCF%2C3AUmmVu7wsx1EvUr1vlsk9%2C3GGyZui8oFJsIwUw7aUqNl%2C3MZsBdqDrRTJihTHQrO6Dq%2C3Ri4H12KFyu98LMjSoij5V%2C3TVXtAsR1Inumwj472S9r4%2C3hKL6z5S9v7AKEydB6wFtQ%2C3hjgDpzMEj8wWDo8vXqywg%2C3nFkdlSjzX9mRTtwJOzDYB%2C3uwAm6vQy7kWPS2bciKWx9%2C3xByNj8XW17oW0wsJhgzYL%2C3zmfs9cQwzJl575W1ZYXeT%2C432R46LaYsJZV2Gmc4jUV5%2C48Mg7JaclPFMCGf4tXdPQn%2C49bzE5vRBRIota4qeHtQM8%2C4TzGOY9RpErzedN02w8Boh%2C4V8LLVI7PbaPR0K2TGSxFF%2C4eujb0S8BP4Oy9suTA04mE%2C4iBLNOPS6bfWtsxPFmN29w%2C4icpPWgCsyDjSbqgzerUSf%2C4nXOZlYoAD67hF9aUEncMY%2C4pMsA8xkkqFIvUQZnkuuPM%2C4tususHNaR68xdgLstlGBA%2C4xHt2cdyWt0XKakPuT4NR2%2C4xaF2VIGwhWyEMbM6GuLdm%2C52QGI02zPXMbtKgi3bOQem%2C558zMGW1SDfXPdI862UQ2A%2C57dN52uHvrHOxijzpIgu3E%2C5A9NWhs9ydYZPGgvcWI8Ms%2C5IcR3N7QB1j6KBL8eImZ8m%2C5K4W6rqBFWDnAN6FQUkS6x%2C5dfFr2qhmXQLvHZqg0dynx%2C5iftm9Sk7OBBnVqa7DbICi%2C5imFWt9rzlx5iGqS58ArtO%2C5rDFcvOmq2yjBnw29OrbwD%2C5v2WhpA59TJSdPh7LCx1lN%2C64mPnRMMeudAet0E62ypkx%2C699OTQXzgjhIYAHMy9RyPD%2C6CjQZyM4LDtXlmAK2EiBRq%2C6Wr3hh341P84m3EI8qdn9O%2C6XyY86QOPPrYVGvF9ch6wz%2C6qC5mBbIPNWPhvaVp8rVvp%2C6qO6LhD6FuXK5e2PtfAIMz%2C6xWXlyazDoshKtv12626Kb%2C6zyPKJ4ePhYLsBEy4A6BVX%2C72VPmrCS0XM1be1hMNnVtC%2C72iCiKwu6nu6Qq9emIwzYv%2C77AKJs9SJqxHXbPgtJPKRa%2C7dH8w9flSy9w81ilr0xXWe"





query = "https://api.spotify.com/v1/me/following?type=artist&ids={}".format(ids1)
response = requests.put(query, headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(spotify_token)})
response_json = response.json()
print(response.json)
#for i in response_json["artists"]["items"]:
#    print((i["id"]))


