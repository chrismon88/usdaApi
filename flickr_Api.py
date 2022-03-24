import requests
from pprint import pprint

def get_photo_flickr(user_input):
    url = f"https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key=7525dbfa809ab56fc74ad95ed1b9b249&&text={user_input}&sort=relevance&extras=food&format=json&nojsoncallback=1"
    response = requests.get(url).json()
    id = response['photos']['photo'][0]['id']
    server_id = response['photos']['photo'][0]['server']
    farm_id = response['photos']['photo'][0]['farm']
    secret_data = response['photos']['photo'][0]['secret']
    url_data = f"https://farm{farm_id}.staticflickr.com/{server_id}/{id}_{secret_data}.jpg"

    return url_data





