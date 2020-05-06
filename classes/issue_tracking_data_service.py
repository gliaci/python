import csv
import os


class IssueTrackingDataService:

    def __init__(self):
        pass

    def issuesToClose(self):
        issuesToCloseData = {
            "data": []
        }

        with open(os.path.join('./data/issuetracking', 'issuesToClose.csv')) as issuesToCloseDataFileHandler:
            for row in csv.reader(issuesToCloseDataFileHandler, delimiter=';'):
                issuesToCloseData["data"].append({"idBooking": row[0], "idIssueType": row[1]})

        return issuesToCloseData["data"]


    def issuesToOpen(self):
        issuesToOpenData = {
            "data": []
        }

        with open(os.path.join('./data/issuetracking', 'issuesToOpen.csv')) as issuesToOpenDataFileHandler:
            for row in csv.reader(issuesToOpenDataFileHandler, delimiter=';'):
                issuesToOpenData["data"].append({"idBooking": row[0], "idIssueType": row[1], "queue": row[2]})

        return issuesToOpenData["data"]