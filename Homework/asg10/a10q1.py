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
    log(f"File {fileName} : {'does exist' if fileExistsFlg == True else 'does not exist'}")

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

def writeData(fileName, data)->bool:
    try:
        fileObj = open(fileName, 'w')
        fileObj.write(data)
        fileObj.close()
        return True
    except Exception as e:
        return False
    finally : 
        log("FAIL")

def getExtnDirecotires(specs):
    directoryName, fileExt = [],[]
    for spec in specs:
        if( '.' in spec):
            fileExt.append(spec)
        else:
            directoryName.append(spec)
    return directoryName, fileExt

def main() ->None :
    #showDocumentation()
    addr = "H:\\DIR_EXPT\\"
    ARGS = SYS.argv
    #log(ARGS)
    CLI_FUNCTIONS = {
        'display':lambda ARGS, addr : search(ARGS, addr),
        'copy': lambda ARGS, addr : copy(ARGS, addr)

    }
    command = ARGS[1]
    if command in CLI_FUNCTIONS:
        CLI_FUNCTIONS[command](ARGS, addr)
    else:
        log(f'No valid command provided \n Please check args {ARGS[1:]}')

def search(ARGS, searchPath) -> None:
    fileCount = 0
    directoryNames, fileExt = getExtnDirecotires(ARGS[2:])
    log(directoryNames)
    for directoryName in directoryNames: 
        for addr, folder, files in OS.walk(f"{searchPath}"):
            for file in files:
                for ext in fileExt:
                    if(file.endswith(ext)):
                        fileCount+=1
                        log("{:<5} {:<25} {:<50}".format(fileCount, file, f"{addr}\{file}"))
    log(f'Total : {fileCount} files found that have {fileExt}')
    return None

def copy(ARGS, searchPath):
    directoryNames, fileExt = getExtnDirecotires(ARGS[2:])
    pickDir, tgtDir = '',''
    if len(directoryNames) == 2:
        pickDir, tgtDir = directoryNames[0], directoryNames[1]
    else:
        return False

    for path, dirName, files in OS.walk(searchPath):
        if pickDir in path:
            for file in files:
                fileObj = open(f"{path}\{file}", 'r')
                fileData = fileObj.read()
                pathArr = path.split('\\')
                
                #print(pathArr)
                tgtFileObj = open(f"{searchPath}{tgtDir}\\{file}", 'w')
                tgtFileObj.write(fileData)
    return True

if __name__ == '__main__':
    main()
