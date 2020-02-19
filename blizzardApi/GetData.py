from constants import constants


class GetData:
    def __init__(self, authorized, requests_class):
        self.authorized = authorized
        self.requests_class = requests_class

    def initialized(self):
        return self.authorized

    def authorize(self):
        self.requests_class.get_auth_token()
        self.authorized = True

    def get_connected_realms_index(self):
        url = f"{constants.URL_HEAD}{constants.REGION}{constants.API_URL}connected-realm/index{constants.API_END}"
        data = self.requests_class.make_request('GET', url)
        print("=========================== DATA ======================")
        print(data)
        print("=======================================================")
        return data

    def get_connected_realms(self, index):
        url = f"{constants.URL_HEAD}{constants.REGION}{constants.API_URL}connected-realm/{index}{constants.API_END}"
        data = self.requests_class.make_request('GET', url)
        print("=========================== DATA ======================")
        print(data)
        print("=======================================================")
        return data
