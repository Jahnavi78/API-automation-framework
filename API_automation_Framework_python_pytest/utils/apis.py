import requests

class APIS:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.header= {
            "Content-Type": "application/json"
        }

    def get(self, endpoint):
        url = f'{self.BASE_URL}/{endpoint}'
        return requests.get(url, headers=self.header)
        #response = requests.get(url, headers=self.header)
        #return response
