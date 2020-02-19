import multiprocessing


def getSquare(numList, queue):
    for n in numList:
        queue.put(n*n)

if __name__ == '__main__':
    numbers = [1,2,3,4,5]
    sharedQueue = multiprocessing.Queue() 
    print("Status of Queue: " , sharedQueue.empty())
    sharedQueue.put(88)
    print("Before process 1")
    print("Status of Queue: " , sharedQueue.empty())
    while sharedQueue.empty() is False:
        print(sharedQueue.get())
    process1 = multiprocessing.Process(target=getSquare, args=(numbers, sharedQueue))
    process1.start()
    process1.join()

    print("After process 1")
    print("Status of Queue: " , sharedQueue.empty())
    while sharedQueue.empty() is False:
        print(sharedQueue.get())
    
    