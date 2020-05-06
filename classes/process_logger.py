from datetime import datetime

from classes.file_system import FileSystem


class ProcessLogger:
    def __init__(self, folder, reportFileName):
        self.startTimestamp = datetime.utcnow()

        self.saveFolderPath = "/tmp/" + folder + "/"
        processReportFilename = self.startTimestamp.strftime('%Y_%m_%d_%H_%M_%S_%f') + "_ProcessReport_" + reportFileName + ".txt"

        processReportFilePath = self.saveFolderPath + processReportFilename

        self.fileSystemObj = FileSystem()
        self.fileSystemObj.makeDirsIfNotExists(processReportFilePath)
        self.processReportFileHandler = open(processReportFilePath, 'w')

    def startProcess(self):
        self.startTimestamp = datetime.utcnow()
        startProcessLog = "PROCESS Start at [{}]".format(self.startTimestamp.strftime('%Y-%m-%d %H:%M:%S.%f'))
        print(startProcessLog)
        self.processReportFileHandler.writelines(startProcessLog + "\n")

    def logProcessMessage(self, message):
        print(message)
        self.processReportFileHandler.writelines(message + "\n")

    def endProcess(self):
        endTimestamp = datetime.utcnow()
        endProcessLog = "PROCESS End at [{}] - duration [{}]".format(endTimestamp.strftime('%Y-%m-%d %H:%M:%S.%f'),
                                                                     self.__getDuration(endTimestamp))
        print(endProcessLog)
        self.processReportFileHandler.writelines(endProcessLog + "\n")
        self.processReportFileHandler.close()

        self.fileSystemObj.openInFinder(self.saveFolderPath)

    def __getDuration(self, endTimestamp):
        diff = endTimestamp - self.startTimestamp
        return "{} h:mm:ss:ms".format(diff)
