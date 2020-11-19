import requests

def downloadThumbnail(url):
    id = url.split('=',1)[1]
    thumbUrl = 'https://img.youtube.com/vi/'+ id + '/maxresdefault.jpg'
    path = './thumbnail' + id + '.jpg'
    thumb = requests.get(thumbUrl)
    with open(path, 'wb') as f:
        f.write(thumb.content)

url = input('Enter video url that you want to download the thumbnail of: ')
print("Downloading . . .")
downloadThumbnail(url)
print('Thumbnail downloaded!')
