import requests

from classes import issue_tracking_service as issueTrackingService


openIssueRequestTemplate = "{{\"idBooking\":{idBooking},\"idIssueType\":{idIssueType},\"queue\":\"{queue}\",\"user\":\"system\",\"topUrgent\":true}}"


class IssueTrackingOpenService:

    def __init__(self, endopoint):
        self.url = endopoint + "open"

    def execute(self, idBooking, idIssueType, queue):
        request = openIssueRequestTemplate.format(idBooking=idBooking, idIssueType=idIssueType, queue=queue)
        return requests.post(self.url, headers=issueTrackingService.headers, data=request)
