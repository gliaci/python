import os
import errno
import subprocess

class FileSystem:

    def __init__(self):
        pass

    def makeDirsIfNotExists(self, filePath):
        if not os.path.exists(os.path.dirname(filePath)):
            try:
                os.makedirs(os.path.dirname(filePath))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise

    def openInFinder(self, folderPath):
        subprocess.Popen(["open", folderPath])

