a = {
    '1':'1',
    '2':'2',
    '3':'3',
    '4':'4',
}

def printer(Obj : dict):
    s = f""
    for key in Obj :
        s += f"{key : <5} "
    s+="\r"
    print(s, end="\r")
i=0
while i != 10000000 :
    printer(a)
