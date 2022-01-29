import os as OS
def main():
    print('Enter file name to create')
    name="demo.txt"
    
    fd = open(name,"w") #rwax
    print(type(fd))
    print(f"File gets created with information as , {fd}")
    data = "SagarPatil"
    fd.write(data)
    #data = fd.read(5)
    fd.close()
    print(data)
    if( OS.path.exists(name)):
        fd = open(name,"rb")
        data = fd.read(5)
        fd.seek(-5,1)
        data = fd.read(5)
        print(data)
        print(f'cuyrrent offset is {fd.tell()}')
        fd.close()
        #OS.remove(name)
    else:
        print("no such file")
    fd.close()
if __name__ == '__main__':
    main()