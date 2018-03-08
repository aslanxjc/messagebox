#-*-coding:utf-8 -*-
import time
import tornado.websocket
from .messagebox import Receiver,sender
import Queue
import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xydian.settings")

from django_redis import get_redis_connection
from utils._t import Seeker,Hider,cond
#print openid_queue.get()
seeker = None
hider = None


redis_client = get_redis_connection("default")
openid_queue = Queue.Queue(1)
socket_queue = Queue.Queue(1)

global socket_queue 
socket_queue = []

class WeChatMessageHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True


    def open(self,openid=None):

        topic = "mpnotify"
        sub = Receiver(self.on_message, topic.encode('utf-8'))




    def on_close(self):
        pass


    def on_message(self, message):
        #TODO heartbeat
        print message,777777777777777777777777777
        #print self.ws_connection.close(),2222222222222222222


    def callback(self, msg):
        pass


class FwhWeChatMessageHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True


    def open(self,openid=None):

        topic = "mpnotify"
        sub = Receiver(self.on_message, topic.encode('utf-8'))




    def on_close(self):
        pass


    def on_message(self, message):
        #TODO heartbeat
        print message,777777777777777777777777777
        #print self.ws_connection.close(),2222222222222222222


    def callback(self, msg):
        pass



class QrWchatMessageHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True


    def open(self,openid=None):

        topic = "mpnotify"
        sub = Receiver(self.on_message, topic.encode('utf-8'))




    def on_close(self):
        pass


    def on_message(self, message):
        #TODO heartbeat
        print message,777777777777777777777777777
        #print self.ws_connection.close(),2222222222222222222


    def callback(self, msg):
        pass

class AlipayMessageHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True


    def open(self):
        #topic = self.get_query_argument('topic')
        #print topic
        topic = "alipaynotify"
        sub = Receiver(self.on_message, topic.encode('utf-8'))


    def on_close(self):
        pass


    def on_message(self, message):
        #TODO heartbeat
        pass


    def callback(self, msg):
        pass


class WxpayMessageHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True


    def open(self):
        #topic = self.get_query_argument('topic')
        #print topic
        topic = "wxpaynotify"
        sub = Receiver(self.on_message, topic.encode('utf-8'))


    def on_close(self):
        pass


    def on_message(self, message):
        #TODO heartbeat
        pass


    def callback(self, msg):
        print 4444444444444444444444
        pass



##################################################
class QrWeChatCallbackHandler(QrWchatMessageHandler):
    def open(self,topic=None):
        print "topic come:",topic 

        socket_queue.append(self.ws_connection)

        if len(socket_queue)<=1:
            self.write_message("open")

        print socket_queue
        sub = Receiver(self.on_message, topic.encode("utf-8"))


        #if socket_queue.empty():
        #    #socket_queue.put(self.ws_connection)
        #    socket_queue.append(self.ws_connection)
        #    sub = Receiver(self.on_message, topic.encode("utf-8"))
        #else:
        #    time.sleep(30)
        #    socket_queue.get().close()
        #    sub = Receiver(self.on_message, topic.encode("utf-8"))


        #if openid_queue.empty():
        #    sub = Receiver(self.on_message, topic.encode("utf-8"))
        #    time.sleep(30)
        #    print self.ws_connection.close(),2222222222222222222
        #else:
        #    sub = Receiver(self.on_message, topic.encode("utf-8"))


    def on_message(self, message):
        print message,7777777777777777
        if message == "close":
            #print self.ws_connection.close(),2222222222222222222
            #socket_queue.get().close()

            socket_queue.remove(self.ws_connection)
            self.ws_connection.close()

            print socket_queue,666666666666666666666
            #print dir(self.ws_connection)

            socket_queue.reverse()
            if len(socket_queue)>1:
                socket_queue.pop().write_message("open")
            else:
                socket_queue[0].write_message("open")
        self.write_message(message)


class WeChatCallbackHandler(WeChatMessageHandler):

    def open(self,openid=None):

        topic = "mpnotify"
        sub = Receiver(self.on_message, topic.encode('utf-8'))

    def on_message(self, message):
        if len(message)>13:
            self.write_message(message)
            self.ws_connection.close()


class FwhWeChatCallbackHandler(FwhWeChatMessageHandler):
    def on_message(self, message): 
        if len(message)>13:
            self.write_message(message)
        print message,55555555555555555555555555


class AlipayCallbackHandler(AlipayMessageHandler):
    def on_message(self, message):
        self.write_message(message)

class WxpayCallbackHandler(WxpayMessageHandler):
    def on_message(self, message):
        self.write_message(message)
