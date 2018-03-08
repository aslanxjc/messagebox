import zmq
import time
from zmq.eventloop import zmqstream
from zmq.eventloop import ioloop
from zmq import ssh

ioloop.install()


class Sender:
    def __init__(self, host='localhost', port=5559, remote_ssh='root@127.0.0.1:22'):
        '''
        @param topic: keep same with Receiver init 'topic' arg.
        '''
        self.host = host
        self.port = port
        self.remote_ssh = remote_ssh

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.connect("tcp://{}:{}".format(self.host, self.port))
        #ssh.tunnel_connection(self.socket, "tcp://{}:{}".format(self.host, self.port), self.remote_ssh)


    def send(self, topic, message):
        print topic,3333333333333333
        self.socket.send("{} {}".format(topic, message))



class Receiver:
    def __init__(self, callback, topic, host='localhost', port=5560, remote_ssh='root@127.0.0.1:22'):
        self.host = host
        self.port = port
        self.callback = callback
        self.remote_ssh = remote_ssh

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect("tcp://{}:{}".format(self.host, self.port))
        #ssh.tunnel_connection(self.socket, "tcp://{}:{}".format(self.host, self.port), self.remote_ssh)
        self.socket.setsockopt(zmq.SUBSCRIBE, topic)
        #self.socket.setsockopt(zmq.SUBSCRIBE, "test")

        self.stream_sub = zmqstream.ZMQStream(self.socket)
        self.stream_sub.on_recv(self.recv_message) 


    def recv_message(self, message):
        print 9999999999999
        print message
        self.callback(message[0])


    def close(self):
        self.stream_sub.close()
        self.socket.close()
        self.context.term()


# http://stackoverflow.com/questions/19442970/zeromq-have-to-sleep-before-send
#
# consider the time used by tcp connect, we should init socket at the beginning
# rather than every time invoke socket.send method, in case of lost message.
# And, it's diffcult to use req/rep to sync pub/sub cause I can't specify a 
# fixed port.
sender = Sender()
