from multiprocessing import Process

def proc_1():
    while 1:
        print("this is the thread 1")
def proc_2():
    while 1:
        print("this is the thread 2")


t1 = Process(target=proc_1)
t2 = Process(target=proc_2)
t1.start()
t2.start()
while 1:
    print("this is the main")
