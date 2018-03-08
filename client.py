import sys
import zmq
from zmq import ssh
port = "5560"
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
print "Collecting updates from server..."
socket.connect ("tcp://localhost:%s" % port)
#ssh.tunnel_connection(socket, "tcp://{}:{}".format('127.0.0.1', port), 'root@127.0.0.1:22')
topicfilter = "9"
socket.setsockopt(zmq.SUBSCRIBE, topicfilter)
for update_nbr in range(10):
    string = socket.recv()
    topic, messagedata = string.split()
    print topic, messagedata
