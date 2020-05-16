from time import sleep
from threading import *


class Hello(Thread):
    # To use Thread we need to use "run" method. Other name will not work here
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


T1 = Hello()
T2 = Hi()

# Start is internal method of Thread
T1.start()
# To avoid the collision
sleep(0.2)
T2.start()

# This will print after completion of both Thread. In here we are saying wait for other thread by using join
T1.join()
T2.join()
print("Bye")
