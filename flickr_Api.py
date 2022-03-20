import requests
from pprint import pprint


key = "7525dbfa809ab56fc74ad95ed1b9b249"

secret = '5089e2b6ded3d0e3'




def get_photo_flickr(user_input):
    url = "https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key=7525dbfa809ab56fc74ad95ed1b9b249&tags= " \
          f"{user_input}+&text={user_input}&sort=relevance+&accuracy=100%25&format=json&nojsoncallback=1"

    response = requests.get(url).json()

    id = response['photos']['photo'][1]['id']
    server_id = response['photos']['photo'][1]['server']
    farm_id = response['photos']['photo'][1]['farm']
    secret_data = response['photos']['photo'][1]['secret']
    url_data = f"https://farm{farm_id}.staticflickr.com/{server_id}/{id}_{secret_data}.jpg"

    return url_data





