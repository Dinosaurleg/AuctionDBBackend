import requests
from requests.auth import HTTPBasicAuth
import json
from constants import constants

with open("config/config.json", "r") as conf:
    config = json.load(conf)

CLIENT_ID = config["clientId"]
ACCESS_INFO = {}


class RequestsClass:
    def get_auth_token(self):
        global ACCESS_INFO
        url = constants.URL_HEAD + constants.REGION + constants.URL_END + constants.TOKEN
        ACCESS_INFO = self.make_request("AUTH", url)
        if ACCESS_INFO:
            print("You're authorized!")

    def make_request(self, type, url, headers={}, options=[]):
        global ACCESS_INFO
        if (type == "AUTH"):
            data = {
                "grant_type": "client_credentials",
            }
            try:
                req = requests.post(url, auth=HTTPBasicAuth(CLIENT_ID, config["clientSecret"]), data=data)
                return req.json()
            except requests.exceptions.RequestException as exc:
                print("Error: " + exc)
        elif not ACCESS_INFO:
            print("Not authorized.")
            return
        else:
            if (type == "GET"):
                try:
                    req = requests.get(url + ACCESS_INFO["access_token"], headers=headers)
                    return req.json();
                except requests.exceptions.RequestException as exc:
                    print("Error: " + exc)
                    return
            elif (type == "POST"):
                try:
                    req = requests.get(url, headers=headers)
                    return req.json()
                except requests.exceptions.RequestException as exc:
                    print("Error: ")
                    print(exc)
