import requests
import json

class HttpController:
    def get(self, originalUrl, params):
        result = None
        response = requests.get(url=originalUrl, params=params)

        if response.status_code == 200:
            result = response.json()

        return result

    def post(self, originalUrl, params):
        result = None
        response = requests.post(url=originalUrl, data=json.dumps(params), headers={'Content-Type': 'application/json'})

        if response.status_code == 200:
            result = response.json()

        return result
