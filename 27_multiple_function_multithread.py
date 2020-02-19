import threading
import time

def getSquare(numList):
    print("Calculate Square of Numbers")
    for n in numList:
        time.sleep(1)
        print("Square: " , n*n)


def getCube(numList):
    print("Calculate Cube of Numbers")
    for n in numList:
        time.sleep(1)
        print("Cube: ",n*n*n)

t = time.time()
numbers = [1,2,3,4,5]
# Single threaded execution!
print('{:-^80}'.format("Single Threaded Execution"))
getSquare(numbers)
getCube(numbers)
print("Time to Execute in Single Thread is: ", time.time() - t)

t = time.time()
print('{:-^80}'.format("Multi Threaded Execution"))
thread1 = threading.Thread(target=getSquare, args=(numbers,))
thread2 = threading.Thread(target=getCube, args=(numbers,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Time to Execute in Multithread is: ", time.time() - t)
print("Done with Maths! Exhausted NOW!")

