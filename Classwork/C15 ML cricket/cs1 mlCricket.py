from sklearn import tree
import matplotlib.pyplot as PLT
def guess(weight, surface) -> str:
    ballFeatures = [
        [35,1], [47,1], [90,0], [48,1], [90,0],
        [35,1], [92,0], [35,1], [35,1], [35,1],
        [96,0], [43,1], [110,0],[35,1], [95,0]
    ]
    names = [ 1,1,2,1,2, 1,2,1,1,1, 2,1,2,1,2 ]
    #print([row[0] for row in ballFeatures])
    weights = [row[0] for row in ballFeatures]
    surfaces = [row[1] for row in ballFeatures]

    #PLT.scatter(x=weights,y=surfaces,c='blue')
    #PLT.show()

    CLASSIFIER = tree.DecisionTreeClassifier()

    CLASSIFIER = CLASSIFIER.fit(ballFeatures, names) 
    result = CLASSIFIER.predict([[weight, surface]])
    return f"Type of ball is {'Tennis Ball' if result == 1 else 'Cricket Ball'}"



def main() -> int:
    """strSurface:str = getValidStdIN(
            "Enter type of surface of ball",
            ["smooth", "0","rough",  "1"]
        )
    surface = 0
    if strSurface.lower() == 'rough' or strSurface.lower() == '1':
        surface = 1
    weight = int(input("Enter weight of ball"))"""
    

    surface = 1
    weight = 35
    print(guess(weight, surface))
    return 0

def getValidStdIN(requestMsg='', validInputTypes=[], validInputs=[]):
    """
    if len(validInputs)>0:
        while(INPUT not in validInputs):
            print(f"Invalid Input. Valid Inputs are \n{validInputs}")
            print(requestMsg)
            INPUT = input()
    return INPUT
    """
    print(requestMsg)
    INPUT = input()
    isInputValid = False
    while not isInputValid :
        if( 
            len(validInputTypes) == 0 
            or len(validInputs) == 0
        ):
            isInputValid = True
        else:
            if len(validInputTypes) > 0:
                pass

if __name__ == '__main__':
    res = main()
    print(f'Program exited with code {res}')