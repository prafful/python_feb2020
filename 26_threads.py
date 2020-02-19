import threading
import time

def callMeForEachThread(threadName, delay):
    counter = 0
    while counter <= 10:
        print("Thread Name:" + threadName + " with counter value: " + str(counter) + " at time: " + str(time.time()))  
        time.sleep(delay)
        counter += 1      

thread1 = threading.Thread(target=callMeForEachThread, args=("Thread1", 1))
thread2 = threading.Thread(target=callMeForEachThread, args=("Thread2", 3))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Multithreading Finished!")


