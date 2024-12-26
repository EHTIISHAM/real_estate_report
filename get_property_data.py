# attom api data collection script

import requests
import os
import json
import time
import pandas as pd

# set up the api key
api_key = os.environ.get('ATTOM_API_KEY')

# set up the base url
get_property_info_url = 'https://api.gateway.attomdata.com/propertyapi/v1.0.0/property/basicprofile'

# set up the headers
headers = {
    'accept': 'application/json',
    'apikey': api_key
}

# set up the payload
payload = {
    'address1': '',
    'address2': '',
}

sample_address12 = ['110 Vandelinda Avenue','Teaneck, NJ 07666']

payload['address1'] = sample_address12[0]
payload['address2'] = sample_address12[1]

# make the request
response = requests.get(get_property_info_url, headers=headers, params=payload)

# get the data
data = response.json()

# print the data
print(json.dumps(data, indent=4))
