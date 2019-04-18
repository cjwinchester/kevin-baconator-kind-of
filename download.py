import os

import requests


URLS = [
    'https://datasets.imdbws.com/name.basics.tsv.gz',
    'https://datasets.imdbws.com/title.principals.tsv.gz',
    'https://datasets.imdbws.com/title.basics.tsv.gz'
]

this_path = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(this_path, 'data')

for url in URLS:
    filename = url.split('/')[-1]
    file_path = os.path.join(data_dir, filename)

    if os.path.isfile(file_path):
        continue

    r = requests.get(url, stream=True)

    with open(file_path, 'wb') as f:
        for chunk in r:
            f.write(chunk)
