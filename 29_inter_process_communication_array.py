import time
import multiprocessing


def getSquare(numList, ress, sc):
    print(numList)
    print(ress)
    sc.value += 1
    for index, n in enumerate(numList):
        print(index, " ", n)
        ress[index] = n*n
    print("Result in process1: ", list(ress), " Score: ", sc.value )    
   

if __name__ == '__main__':
    numbers = [1,2,3,4,5]
    #datatype and size    
    result = multiprocessing.Array('i', 5)
    score = multiprocessing.Value('d', 0.0)
    print("Value of score in main Process Before: ", score.value)
    print("Result List in Main Process Before: ", list(result))
    process1 = multiprocessing.Process(target=getSquare, args=(numbers, result, score))
    process1.start()
    process1.join()
    print("Value of score in main Process After: ", score.value)
    print("Result List in Main Process After: ", list(result))    
    print("Done with multiprocessing!")