from threading import Timer
loader_items = {
    '0':' | ',
    '1':' / ',
    '2':' - ',
    '3':' \ ',
}
def generateLoader():
    for key in loader_items:
        yield(loader_items[key])
        
def showLoader():
    for key in generateLoader():
        print(loader_items[key])

def main():
    #showLoader()
    t1 = Timer(1.0, showLoader, ())
    t1.start()


if __name__ == '__main__':
    main()