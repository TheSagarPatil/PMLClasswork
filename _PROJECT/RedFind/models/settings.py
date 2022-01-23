import json as JSON

from interfaces.Isettings import ISETTINGS
class Settings(object):
    def __init__(self, path:str ):
        self.settingsFile = open(path)
        self.settings:ISETTINGS =  JSON.load(self.settingsFile)
        self.settingsFile.close()

    def getSettings(self):
        return self.settings
