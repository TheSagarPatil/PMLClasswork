import time as TIME
import multiprocessing as MP
def processFunk(x):
    
    TIME.sleep(0.25)
    print(f'{MP.current_process().name} {x}')

def main():
    processes = list()
    #print('single process thread app')
    #startTime = TIME.time()
    for i in range(10):
        p = MP.Process(target=processFunk, args=(i,), name='A')
        processes.append(p)
        p.start()

    for process in processes:
        process.join()
        
    for process in processes:
        process.close()
        
    #print(f'Performance : {startTime - TIME.time()}')

if __name__ == '__main__':
    main()
