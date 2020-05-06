import os


class CsvData:

    def __init__(self):
        pass

    def getAirlineIds(self):
        return self.__getData('airlineIds.csv')

    def getMarkets(self):
        return self.__getData('markets.csv')

    def __getData(self, filename):
        fileHandler = open(os.path.join('./data', filename), 'r')
        data = fileHandler.read().splitlines()
        fileHandler.close()
        return data
