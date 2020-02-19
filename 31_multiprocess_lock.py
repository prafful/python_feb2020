import multiprocessing
import time

def depositMoney(money, lock):
    for i in range(50):
        time.sleep(0.5)
        lock.acquire()
        money.value += 1
        lock.release()
        print("Deposited! ", money.value)


def withdrawMoney(money, lock):
    for i in range(50):
        time.sleep(0.5)
        lock.acquire()
        money.value -= 1
        lock.release()
        print("Withdrawn! ", money.value)


if __name__ == "__main__":
    lockProcess = multiprocessing.Lock()
    balanceMoney = multiprocessing.Value('i', 0)
    process1 = multiprocessing.Process(target=depositMoney, args=(balanceMoney, lockProcess))
    process2 = multiprocessing.Process(target=withdrawMoney, args=(balanceMoney, lockProcess))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Final Balance: ", balanceMoney.value)