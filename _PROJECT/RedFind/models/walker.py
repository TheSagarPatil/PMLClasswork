from msilib.schema import Error
import os as OS
import time as T
import hashlib as H
import json as JSON
class Walker(object):
    def __init__(self, path:str =None):
        print(f'RedFinder : Walker is ON')
        self.path = path or "G:/A"
        self.walked_files = {}
        self.duplicate_files = {}

    def walk(self):
        md5_initializer = H.md5
        
        for root, dirs, files in OS.walk(self.path):
            for file in files:
            
                MD5 = md5_initializer()
                BLOCK_SIZE = 128 * MD5.block_size
                filepath =root+"\\"+file
                
                OPEN_FILE = open(filepath, 'rb')
                try:
                    chunk = OPEN_FILE.read(BLOCK_SIZE)
                    while chunk:
                        MD5.update(chunk)
                        chunk = OPEN_FILE.read(BLOCK_SIZE)
                    MD5_HASH = MD5.hexdigest()
                    OPEN_FILE.close()
                    print(f'Opening {MD5_HASH} : {filepath} : ', end='\n')
                    if MD5_HASH not in self.walked_files:
                        #print('not duplicate')
                        paths = []
                        paths.append(filepath)
                        self.walked_files[MD5_HASH] = paths
                        continue
                    if MD5_HASH in self.walked_files:
                        
                        #paths = self.duplicate_files[MD5_HASH]
                        paths= []
                        if MD5_HASH in self.duplicate_files:
                            paths=[*paths, *self.duplicate_files[MD5_HASH] ]
                        print('duplicate')
                        paths.append(filepath)
                        self.duplicate_files[MD5_HASH] = paths
                        print(self.duplicate_files[MD5_HASH])
                except Exception as e:
                    print(f'{e} File error has occured {filepath}\n')
            #print(f'Exists {MD5_HASH in self.walked_files}')
            #print(f'Current Directory : {root}', end = '\r')
            #T.sleep(0.01)
        
        print('\nEnd of walk00', self.walked_files)
        #print(JSON.dumps(self.walked_files, indent=2))
        report = self.duplicate_files 
        print(report)
        return report
        
        
        

