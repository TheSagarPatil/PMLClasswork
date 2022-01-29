import sys as SYS
import os as OS
#check if file exists or not

def showDocumentation():
    help(fileExists)
    help(printIfFileExist)

def log(*args):
    print('Out >>', *args)

def printIfFileExist( fileExistsFlg :bool , fileName : str )->None:
    """ 
    @Help 
        @Author : Sagar Patil (Github : @TheSagarPatil)
        @ContributorAuthors : []
        @Param : fileExistsFlg -> bool
        @Param : fileName -> str
        @Returns : None
        @Algorithm : Checks if file exits or not and prints <file name> exits or not accordingly
    """
    log(f"File {fileName} : {'exists' if fileExistsFlg == True else 'does not exist'}")

def fileExists( INPUT_FILE : str )->bool:
    """ 
    @Help 
        @Author : Sagar Patil (Github : @TheSagarPatil)
        @ContributorAuthors : []
        @Param : INPUT_FILE -> str
        @Returns : fileExits -> bool
        @Algorithm : Checks if file exits or not and returns true false accordingly
    """
    return True if OS.path.exists(INPUT_FILE) else False

def readFileData(INPUT_FILE_NAME):
    """ 
    @Help 
        @Author : Sagar Patil (Github : @TheSagarPatil)
        @ContributorAuthors : []
        @Param : INPUT_FILE_NAME -> str
        @Returns : FileData -> str, none
        @Algorithm : reads data from given file name, and returns filedata
    """
    fileObj = open(INPUT_FILE_NAME, 'r')
    data = fileObj.read()
    fileObj.close()
    return data

def printFileData(fileName, data):
    log(f"Data in file is \n{data}")
    log(f"End of file {fileName}")

def copyData(fileName, data):
    fileObj = open(fileName, 'w')
    fileObj.write(data)
    fileObj.close()

def main() ->None :
    #showDocumentation()
    ARGS = SYS.argv
    #log(ARGS)
    if len(ARGS) == 2:
        INPUT_FILE = ARGS[1]
        fileExist = fileExists(INPUT_FILE)
        printIfFileExist(fileExist, INPUT_FILE)
        if(fileExist):
            data = readFileData(INPUT_FILE)
            printFileData(INPUT_FILE, data)
            copyData("abcd.txt", data)
    else:
        log('No file provided')

if __name__ == '__main__':
    main()
