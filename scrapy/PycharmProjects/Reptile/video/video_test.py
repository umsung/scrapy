import requests

def savefile():
    f = open('1.mp4', 'ab')
    print('kaishi')
    f.write(requests.get('https://video.asos-media.com/products/ASOS/_media_/031/031922b0-79a7-4bab-acd5-2f0b8355dd68.mp4').content)
    f.close()


savefile()