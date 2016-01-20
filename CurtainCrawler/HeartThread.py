import threading
import time
import MessageHandler

__author__ = 'wangzi6147'


class HeartThread(threading.Thread):
    def __init__(self, socket, interval):
        threading.Thread.__init__(self)
        self.socket = socket
        self.interval = interval

    def run(self):
        while (1):
            print 'heart beat'
            self.socket.send(MessageHandler.build('type@=keeplive/tick@=%{0}/'.format(int(time.time()))))
            time.sleep(self.interval)
