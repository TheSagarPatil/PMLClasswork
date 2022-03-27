import copy
from unicodedata import name
import pandas as PD
import numpy as NP
import matplotlib.pyplot as PLT
import multiprocessing as MP

D_COLOR_MAP = {
    1 : 'r',
    2 : 'g',
    3 : 'b'
}

def showGraph(func) -> None:
    p1 = MP.Process(
        target=func,
        args=(),
        name='Process1'
    )
    p1.start()

def main():
    processes : list= list()
    process_count : int = 0

    df =  getData()

    printTitle('Training DS')
    print(" Step 1 : K means (centeroid) initialized ")
    NP.random.seed(200)
    k = 3
    #centeroids[i]=[x,y]
    centeroids = {
        i+1 : [NP.random.randint(0, 80), NP.random.randint(0, 80)]
        for i in range(k)
    }


    printTitle("Random Centeroids Generated")
    print(centeroids)

    fig = PLT.figure( figsize = (5, 5) )
    PLT.scatter(df['x'], df['y'], color='k')
    for i in centeroids:
        PLT.scatter( *centeroids[i], color = D_COLOR_MAP[i])
    PLT.title('Random Centeroids dataset')
    #showGraph(PLT.show)
    P1 : MP.Process  = MP.Process(
        name = f'GraphG{process_count}',
        target= PLT.show,
        args=()
    )

    processes.append( P1 )
    for p in processes:
        p.start()
        p.join()

    #processes[process_count].start()
    #PLT.show()









def getData() -> PD.DataFrame :
    return PD.DataFrame({
        'x': [12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72],
        'y': [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24]
    })
def printEndOfSection(l = 50) -> None:
    print('-' * l)

def printTitle(*kwargs) -> None:
    print('-' * 50)
    if len(kwargs) > 1:
        print( kwargs )
    else :
        print( *kwargs )
    print('-' * 50)

if __name__ == '__main__':
    main()
