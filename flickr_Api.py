import requests
from pprint import pprint

# from app import search


key = "7525dbfa809ab56fc74ad95ed1b9b249"

secret = '5089e2b6ded3d0e3'

url = " https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key=7525dbfa809ab56fc74ad95ed1b9b249&text=" \
      f"apple&format=json&nojsoncallback=1"


# response = requests.get(url).json()
# pprint(response['photos'])
# pprint(response)
def get_photo_flickr(user_input):
    url = " https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key=7525dbfa809ab56fc74ad95ed1b9b249&text=" \
          f"{user_input}&format=json&nojsoncallback=1"
    response = requests.get(url).json()
    #pprint(response)
    id = response['photos']['photo'][0]['id']
    server_id = response['photos']['photo'][0]['server']
    farm_id = response['photos']['photo'][0]['farm']
    secret_data = response['photos']['photo'][0]['secret']
    url_data = f"https://farm{farm_id}.staticflickr.com/{server_id}/{id}_{secret_data}.jpg"
    #return url_data, id ,server_id, farm_id, secret_data
    #photo_url = "https://farm66.staticflickr.com/65535/51943677656_f97282184b.jpg"
    #return photo_url, url_data, id ,server_id, farm_id, secret_data
    return  url_data

# photo_url = "https://farm66.staticflickr.com/65535/51943677656_f97282184b.jpg"
# response = requests.get(photo_url)
# https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg

# with open('../food_photo.jpg', 'wb') as file:
# for chunk in response.iter_content():
# file.write(chunk)
# flickr = flickrapi.FlickrAPI(key,secret,cache=True)


# def flickr_walk(keyward):
#  quer = search (key, text.n)
#  photos = keyward.walk(text=keyward,
#               tag_mode='all',
#               tags=keyward,
#               extras='url_c',
#               per_page=10,
#               sort='relevance')
#    for photo in photos:
#    try:
#    print(url)
#    except Exception as e:
#    print('failed to download image')
#    with open('../food_photo.jpg', 'wb') as file:
#    for chunk in response.iter_content():
#    file.write(chunk)
# with open('../food_photo.jpg', 'wb') as file:
#  for chunk in response.iter_content():
#     file.write(chunk)
