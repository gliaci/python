import requests

from classes import issue_tracking_service as issueTrackingService


closeIssueRequestTemplate = "{{\"idBooking\": {idBooking},\"user\": \"system\",\"idIssueType\": {idIssueType}}}"


class IssueTrackingCloseService:

    def __init__(self, endpoint):
        self.url = endpoint + "close"

    def execute(self, idBooking, idIssueType):
        request = closeIssueRequestTemplate.format(idBooking=idBooking, idIssueType=idIssueType)
        return requests.put(self.url, headers=issueTrackingService.headers, data=request)