import threading
import time
import socket_message

__author__ = 'wangzi6147'


class HeartThread(threading.Thread):
    def __init__(self, socket, interval):
        threading.Thread.__init__(self)
        self.socket = socket
        self.interval = interval

    def run(self):
        while (1):
            print 'heart beat'
            self.socket.send(socket_message.build('type@=keeplive/tick@=%{0}/'.format(int(time.time()))))
            time.sleep(self.interval)
