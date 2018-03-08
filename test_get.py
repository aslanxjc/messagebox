import Queue
import time

a = Queue.Queue()

#print a.put(1)
for i in range(1,10):
    print i
    a.put(i)
    time.sleep(1)
