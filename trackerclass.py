import requests
from cred import *


class Tracker:
    def __init__(self):
        self.parameters = None
        self.dhldict = None
        self.result = None
        self.tracking_number = None
        self.endpoint = 'https://api-eu.dhl.com/track/shipments'
        self.apikey = API_KEY  # Type in your API-KEy
        self.apisecret = API_SECRET
        self.header = { 'DHL-API-Key': self.apikey }

    def getstatus(self, tracking_number):
        self.tracking_number = tracking_number
        self.parameters = { 'trackingNumber': self.tracking_number }
        raw_data = requests.get(url=self.endpoint, headers=self.header, params=self.parameters)
        raw_data.raise_for_status()
        self.result = raw_data.json()
        self.dhldict = self.result[ 'shipments' ][ 0 ][ 'status' ]
        return self.dhldict
