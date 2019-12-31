# This file is an exercise on multi threading

import threading
import time

t_lock = threading.Lock()


def timer(name, delay, repeat):
    print("Timer: " + name + " started")
    t_lock.acquire()
    print(name + " has acquired the lock")
    while repeat > 0:
        time.sleep(delay)
        print(name + ": " + str(time.ctime(time.time())))
        repeat -= 1
    print(name + " is releasing the lock")
    t_lock.release()
    print("Timer: " + name + " completed")


def main():
    t1 = threading.Thread(target=timer, args=('Timer1', 1, 5))
    t2 = threading.Thread(target=timer, args=('Timer2', 2, 5))
    t1.start()
    t2.start()

    print("Main completed")


if __name__ == '__main__':
    main()
