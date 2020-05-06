from classes.issue_tracking_close_service import IssueTrackingCloseService
from classes.issue_tracking_data_service import IssueTrackingDataService
from classes.issue_tracking_open_service import IssueTrackingOpenService
from classes.process_logger import ProcessLogger

productionEndpoint = "http://production/issuetracking-api/rs/issueTrackingService/"

qaEndpoint = "http://staging/issuetracking-api/rs/issueTrackingService/"

headers = {
    "Content-type": "application/json"
}

class IssueTrackingService:

    def __init__(self, environment):
        self.endpoint = self.__resolveEndpoint(environment)
        self.issueTrackingCloseService = IssueTrackingCloseService(self.endpoint)
        self.issueTrackingOpenService = IssueTrackingOpenService(self.endpoint)
        self.issueTrackingDataService = IssueTrackingDataService()

    def getEndpoint(self):
        return self.endpoint

    def close(self):
        processLogger = ProcessLogger("issuesToClose", "IssuesToClose")
        processLogger.startProcess()

        processOperationIndex = 1
        for issueToCloseData in self.issueTrackingDataService.issuesToClose():
            idBooking = issueToCloseData["idBooking"]
            idIssueType = issueToCloseData["idIssueType"]

            processLogger.logProcessMessage("[{}] Start Close Issue for IdBooking [{}], IdIssueType [{}]...".format(processOperationIndex, idBooking, idIssueType))
            response = self.issueTrackingCloseService.execute(idBooking, idIssueType)
            processLogger.logProcessMessage("[{}] End Close Issue for IdBooking [{}], IdIssueType [{}] with status [{}]".format(processOperationIndex, idBooking, idIssueType, response.status_code))

        processLogger.endProcess()

    def open(self):
        processLogger = ProcessLogger("issuesToOpen", "IssuesToOpen")
        processLogger.startProcess()

        processOperationIndex = 1
        for issueToOpenData in self.issueTrackingDataService.issuesToOpen():
            idBooking = issueToOpenData["idBooking"]
            idIssueType = issueToOpenData["idIssueType"]
            queue = issueToOpenData["queue"]

            processLogger.logProcessMessage(
                "[{}] Start Open Issue for IdBooking [{}], IdIssueType [{}], Queue [{}]...".format(processOperationIndex, idBooking, idIssueType, queue))
            response = self.issueTrackingOpenService.execute(idBooking, idIssueType, queue)
            processLogger.logProcessMessage(
                "[{}] End Open Issue for IdBooking [{}], IdIssueType [{}], Queue [{}] with status [{}]".format(processOperationIndex,
                                                                                                  idBooking,
                                                                                                  idIssueType,
                                                                                                  queue,
                                                                                                  response.status_code))
        processLogger.endProcess()

    def __resolveEndpoint(self, environment):
        if environment is "production":
            return productionEndpoint
        return qaEndpoint