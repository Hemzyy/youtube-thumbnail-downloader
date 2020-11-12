import requests, os, sys
from random import randint

url = input('Enter video url that you want to download the thumbnail of: ')
id = url.split('=',1)[1]
thumbUrl = 'https://img.youtube.com/vi/'+ id + '/maxresdefault.jpg'

print("Downloading . . .")

name = str(randint(0, 999))
path = './thumbnail' + name + '.jpg'
thumb = requests.get(thumbUrl)
with open(path, 'wb') as f:
    f.write(thumb.content)

print('Thumbnail downloaded!')