import requests
import os

url = "https://api.elevenlabs.io/v1/voices/add"
elevenlabs_key = 'YOUR KEY HERE'

directory = 'combined'

headers = {
  "Accept": "application/json",
  "xi-api-key": elevenlabs_key
}

data = {
    'name': 'Goku',
    'labels': '{"accent": "American"}',
    'description': 'Hey its me Goku!'
}

# files = [
#     ('files', ('sample1.mp3', open('sample1.mp3', 'rb'), 'audio/mpeg')),
#     ('files', ('sample2.mp3', open('sample2.mp3', 'rb'), 'audio/mpeg'))
# ]

files = []

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        files.append(('files', (f, open(f, 'rb'), 'audio/mpeg')))

response = requests.post(url, headers=headers, data=data, files=files)
print(response.text)
