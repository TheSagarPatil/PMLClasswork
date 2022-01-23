import sys as SYS
import json as JSON
def  main():
    jsonInput = open('./p4.json')
    var = JSON.load(jsonInput)
    print(var["args"])
if __name__ == '__main__':
    main()