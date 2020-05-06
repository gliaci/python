import json
import os


class DbConnection:

    def __init__(self):
        pass

    def configuration(self):
        return self.__getDbConnection('configurationDbConnectionParameters.json')

    def booking(self):
        return self.__getDbConnection('bookingDbConnectionParameters.json')

    def __getDbConnection(self, filename):
        return json.load(open(os.path.join('./resources', filename), 'r'))
