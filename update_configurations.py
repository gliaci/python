#!/usr/bin/env python3

###########################################################################
# Create an insert script into TOUR_OPERATOR_CONFIGURATIONS table
# using configurations saved into data/tourOperatorConfigurations.csv file
# and data retrieved from the TOUR_OPERATOR_ACTIVATIONS table
# for the Business Profiles in the data/businessProfiles.csv file
###########################################################################

#!/usr/bin/env python3
import csv
import os
from classes.input_handler import InputHandler
from classes.csv_data import CsvData
from classes.db_connection import DbConnection
from classes.tour_operator_service import TourOperatorService
from classes.file_system import FileSystem

inputHandler = InputHandler()

dbUser = inputHandler.inputNotBlankString("Db User")
dbPassword = inputHandler.inputPassword()
marketIndex = inputHandler.inputInRangeNumber("Market (1 = IT | 2 = ES | 3 = FR | 4 = UK | 5 = OTHER): ", 1, 5)
csv_data_obj = CsvData()
market = csv_data_obj.getMarkets()[marketIndex - 1]

bsaDbConnectionParameters = DbConnection().configuration()
clsTourOperatorService = TourOperatorService(bsaDbConnectionParameters, dbUser, dbPassword)

businessProfiles = csv_data_obj.getBusinessProfiles()

activationIds = clsTourOperatorService.getActivationIdsByBusinessProfiles(businessProfiles)

configurations = {
    "configurations": [
    ]
}

with open(os.path.join('./data', 'tourOperatorConfigurations.csv')) as configurationFileHandler:
    for row in csv.reader(configurationFileHandler, delimiter=';'):
        configurations["configurations"].append({"airline": row[0], "fareTypes": row[1]})

deleteConfigurationSql = "DELETE FROM TOUR_OPERATOR_CONFIGURATIONS WHERE ID={};\n"

insertConfigurationSql = "INSERT INTO TOUR_OPERATOR_CONFIGURATIONS (ID_AIRLINE, FARE_TYPES) VALUES ('{}', '{}');\n"

setLastInsertId = "SET {} = (SELECT @last_insert_id);\n"

insertActivationConfigurationSql = "INSERT INTO TOUR_OPERATOR_ACTIVATIONS_CONFIGURATIONS (ID_ACTIVATIONS, ID_CONFIGURATIONS) VALUES ({}, {});\n\n"

saveFolderPath = "/tmp/tour_operator/"
filename = "tourOperatorConfigurations{}.sql".format(market)
filePath = saveFolderPath + filename

fileSystemObj = FileSystem()
fileSystemObj.makeDirsIfNotExists(filePath)

sqlScriptFileHandler = open(filePath, 'w')

activationIdList = []
for activation in activationIds:
    activationIdList.append(str(activation['ID']))

configurationsIdsByActivationIds = clsTourOperatorService.getActivationConfigurationsIdByActivationId(activationIdList)

configurationAirlineIds = []
for configuration in configurations['configurations']:
    configurationAirlineIds.append(configuration['airline'])

configurationIdsByActivationIdsList = []
for configurationIdByActivationIds in configurationsIdsByActivationIds:
    configurationIdsByActivationIdsList.append(str(configurationIdByActivationIds['ID_CONFIGURATIONS']))

configurationIdsToDelete = clsTourOperatorService.getConfigurationIdsByConfigurationIdsAndAirlineIds(
    configurationIdsByActivationIdsList,
    configurationAirlineIds)

for configurationIdToDelete in configurationIdsToDelete:
    sqlScriptFileHandler.writelines(
        deleteConfigurationSql.format(configurationIdToDelete['ID']))

sqlScriptFileHandler.writelines("\n")

configurationId = 1
for activationId in activationIds:
    for configuration in configurations['configurations']:
        sqlScriptFileHandler.writelines(
            insertConfigurationSql.format(configuration['airline'], configuration['fareTypes']))
        configurationIdVariable = "@id_configuration{}".format(configurationId)
        sqlScriptFileHandler.writelines(setLastInsertId.format(configurationIdVariable))
        sqlScriptFileHandler.writelines(
            insertActivationConfigurationSql.format(activationId['ID'], configurationIdVariable))
        configurationId += 1

sqlScriptFileHandler.close()

fileSystemObj.openInFinder(saveFolderPath)
