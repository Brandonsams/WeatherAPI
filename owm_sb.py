import requests
import json

class forecast:
    def __init__(self, json):
        self.json = json

class url:
    def __init__(self,key,**kwargs):
        self.key = key
        # Used to pass city or 
        self.__dict__.update(kwargs)

def zipCodeInput():
    pass

def cityInput():
    pass

def buildUrl():
    pass

def request(url):
    resp = requests.get(url).json()
    return(resp)
