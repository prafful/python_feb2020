import time
import multiprocessing

result = []

def getSquare(numList, ress):
    for n in numList:
        time.sleep(4)
        ress.append(n*n)
        print("Temporary Result List in process1: ", ress)    
        print("Square: ", n*n)
    print("Result List in process1: ", ress)    

""" def getCube(numList, resc):
    for n in numList:
        time.sleep(4)
        cress.append(n*n*n)
        print("Cube: ", n*n*n)        
    print(resc)   """  


print("Result List: ", result)
if __name__ == '__main__':
    numbers = [1,2,3,4,5]

    process1 = multiprocessing.Process(target=getSquare, args=(numbers, result))
    #process2 = multiprocessing.Process(target=getCube, args=(numbers, result))

    process1.start()
    #process2.start()

    process1.join()
    #process2.join()

    print("Result List in Main Process: ", result)    
    print("Done with multiprocessing!")