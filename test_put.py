import Queue
import time
from test_get import a


while True:
    print a.get(timeout=10)
    time.sleep(3)

