from blizzardApi.GetData import GetData
from blizzardApi.RequestsClass import RequestsClass


class BlizzardAPIController:
    def getRealms(self):
        requests_class = RequestsClass()
        data_class = GetData(False, requests_class)
        data_class.authorize()
        data_class.get_connected_realms_index()
        return data_class.get_connected_realms(11)
