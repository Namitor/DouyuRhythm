__author__ = 'wangzi6147'

import socket


class Crawler(object):
    def __init__(self):
        self.socket_ip = '125.88.176.8'
        self.socket_port = 12601
        self.username = 'username'
        self.password = 'password'

    def start(self):
        main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        main_socket.connect((self.socket_ip, self.socket_port))
        main_socket.sendall('type@=loginreq/username@=visitor34807350/password@=1234567890123456/roomid@=25515/"')
        main_socket.sendall('type@=joingroup/rid@=25515/gid@=94/')
        while(1):
            data = main_socket.recv(1024)
            print data





