import os as OS
from sys import argv
from models.walker import Walker
from models.settings import Settings
from interfaces.Isettings import ISETTINGS
import json as JSON 

class APP:
    def __init__(self):
        self.path = self.__getDefaultPath()
    def getSettings(self):
        return Settings(self.path).getSettings()
    def __getDefaultPath(self):
        ARGS = argv
        return ARGS[1] if len(ARGS) > 1 else "./settings.json"

def main():
    S = APP()
    SETTINGS = S.getSettings()
    print(SETTINGS)
    report = print_explorable_paths(SETTINGS['explore_paths'])
    reportDumpable = report #JSON.dumps(report, indent=2)
    writeOperationSuccess = write_report_file(SETTINGS["report_paths"][0], reportDumpable)
    print("Successfully Report Generated" if writeOperationSuccess else "Failed to write file")
    #print(S.__getDefaultPath())

def print_explorable_paths(PATHS):
    print('Explorable paths')
    EXPLORABLE_PATHS = PATHS
    report = {}
    for path in EXPLORABLE_PATHS:
        r = Walker(path).walk()
        print("R = ", r) 
        if not r:
            report.update(r)
    return report 
    
def write_report_file(path, report):
    report_file=open(path,'w')
    #report_file.write(report)
    try :
        report_file.seek(0)
        JSON.dump(report, report_file, indent=2)
    
        report_file.close()
    except:
        print("Unable to write file")
        return False
    return True
if __name__ == '__main__':
    main()