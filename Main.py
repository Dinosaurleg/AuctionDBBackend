from GetData import GetData
from RequestsClass import RequestsClass

class Main:
	if __name__ == '__main__':
		requests_class = RequestsClass()
		data_class = GetData(False, requests_class)
		data_class.authorize()
		data_class.get_connected_realms_index()
		data_class.get_connected_realms(11)