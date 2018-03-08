import zmq
import random
import sys
import time
from zmq import ssh

port = "5559"
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://localhost:%s" % port)
#ssh.tunnel_connection(socket, "tcp://{}:{}".format('127.0.0.1', port), 'root@10.45.237.49:22')
#ssh.tunnel_connection(socket, "tcp://{}:{}".format('127.0.0.1', port), 'root@127.0.0.1:22')
publisher_id = random.randrange(0,9999)
while True:
    topic = random.randrange(8,10)
    messagedata = "server#%s" % publisher_id
    print "%s %s" % (2333, messagedata)
    socket.send("%d %s" % (9, messagedata))
    time.sleep(1)
