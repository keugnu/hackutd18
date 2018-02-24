import requests
import json


class GiphyRequest:
    def __init__(self, query_string, resource, req_type, api_key):
        self.query_string = query_string
        self.resource = resource
        self.api_key = api_key
        self.req_type = req_type


    def send(query_string):
        tx = 'https://api.giphy.com/v1/{}/{}?api_key={}&s={}'.format(self.resource, self.req_type, api_key, query_string)
        rx = requests.get(tx)
        jresp = json.load(rx)
        if rx.status_code == 200:
            embed = jresp['data'][0]['embed_url']
        else:
            embed = 1
        return embed
    

