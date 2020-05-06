#!/usr/bin/env python3

import argparse

from classes.issue_tracking_service import IssueTrackingService

parser = argparse.ArgumentParser(prog="IssueTracking", description='IssueTracking Open / Close Services using csv files into ./data/issuetracking',
                                 usage='python3 issue_tracking.py service (open|close) [-env qa|production]')
parser.add_argument("-env", metavar='environment',
                    default="qa",
                    choices=["qa", "production"],
                    type=str, help="available environments: %(choices)s")
parser.add_argument("service", metavar='service',
                    choices=["close", "open"],
                    type=str, help='available services: %(choices)s')

args = parser.parse_args()

service = args.service
env = args.env
print("Executing [{}] service for [{}] environment...".format(service, env))

issueTrackingServiceObj = IssueTrackingService(env)
print("Endpoint [{}]".format(issueTrackingServiceObj.getEndpoint()))


if "open" == service:
    issueTrackingServiceObj.open()
else:
    issueTrackingServiceObj.close()
