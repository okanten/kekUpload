"""
MIT License (See LICENCE file)

Copyright (c) 2018 Ola Kanten

"""
import requests, base64, pyperclip, sys

DIRECT_URL = 'https://kek.gg/i/'
DERP_URL = 'https://kek.gg/?i/'
URL_API = 'https://u.kek.gg/v1/url-upload-to-kek'
FILE_API = 'https://u.kek.gg/v1/upload-to-kek'

def main():
    clip = pyperclip.paste()
    if len(sys.argv) > 1:
        image = open(sys.argv[1], 'rb')
        uploadImage(FILE_API, 'data:image/png;base64,' + base64.b64encode(image.read()).decode('utf-8')) # We'll send it as png regardless of what it is.
    elif clip[:4] == 'http':
        print('Uploading', clip, 'to kek.gg')
        uploadImage(URL_API, clip)
    elif clip[:10] == 'data:image':
        print('Uploading base64 to kek.gg')
        uploadImage(FILE_API, clip)
    else:
        print('Your clipboard doesnt contain any links and you didnt provide any image as arguments.')

def uploadImage(apiUrl, payload):
    headers = {'Content-Type': 'text/plain'}
    r = requests.post(apiUrl, data=payload, headers=headers)
    if r.text[:16].replace('"', '') == 'https://kek.gg/':
        direct = r.text[1:-1].replace(DERP_URL, DIRECT_URL)
        pyperclip.copy(direct)
        print('Success!\n' + direct)
    else:
        print('Something failed during upload, this is the response from kek.gg:', r.text)

main()
