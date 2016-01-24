# coding=utf-8
import os
import socket
import datetime
import sys
import requests
import socket_message
import time
import uuid
import hashlib
import HTTPUtils
import response_parser

project_path = os.path.dirname(os.path.dirname(__file__))
print 'project path = %s' % project_path
sys.path.append(project_path)

from HeartThread import HeartThread
from dao_utils import db_controller

__author__ = 'wangzi6147'

LOGIN_SERVER = 'http://127.0.0.1:9090/login'


class Crawler(object):
    def __init__(self, url):
        self.socket_ip = '125.88.176.8'
        self.socket_port = 12601
        self.username = 'username'
        self.password = 'password'
        self.roomid = 421867
        self.groupid = 27
        self.url = url

    def start(self):

        # page_html = HTTPUtils.get(self.url)
        page_html = requests.get(self.url).content
        self.roomid = int(response_parser.parse_room_id(page_html))
        server_ip, server_port = response_parser.parse_server_info(page_html)
        # self.login_request(server_ip, server_port)
        self.login_server(server_ip, server_port)

        main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print 'connect'
        main_socket.connect((self.socket_ip, self.socket_port))
        # self.get_groupid(main_socket)
        print 'login'
        main_socket.send(socket_message.build(
            'type@=loginreq/username@=username/password@=password/roomid@={0}/'.format(self.roomid)))
        main_socket.recv(1024)
        print 'join'
        print 'gid=%s' % self.groupid
        main_socket.send(socket_message.build('type@=joingroup/rid@={0}/gid@={1}/'.format(self.roomid, self.groupid)))

        heart_thread = HeartThread(main_socket, 40)
        heart_thread.start()

        while (1):
            userid, nickname, content = response_parser.parse_content(main_socket.recv(1024))
            post_time = datetime.datetime.utcnow()
            if userid != -1:
                # print 'nickname: ' + nickname + ' content: ' + content
                print '[room:%s][%s]%s: %s' % (self.roomid, post_time, nickname, content)
                db_controller.save_danmu(userid, nickname, content, post_time, self.roomid)
                # yield userid, nickname, content, datetime.datetime.utcnow(), self.roomid

    def login_request(self, server_ip, server_port):
        print 'login_server_ip: ' + server_ip + ' login_server_port: ' + server_port
        login_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        login_socket.connect((server_ip, int(server_port)))
        cur_time = str(int(time.time()))
        devid = str(uuid.uuid1()).replace('-', '').upper()
        m = hashlib.md5()
        m.update(str(cur_time) + '7oE9nPEG9xXV69phU31FYCLUagKeYtsF' + devid)
        vk = m.hexdigest()
        login_socket.send(socket_message.build(
            'type@=loginreq/username@=/ct@=0/password@=/roomid@={0}/devid@={1}/rt@={2}/vk@={3}/ver@=20150929/'.format(
                self.roomid, devid, cur_time, vk)))
        while (1):
            response = login_socket.recv(1024)
            rid, gid = response_parser.parse_id(response)
            if rid != '' and gid != -1:
                self.roomid = rid
                self.groupid = gid
                print 'rid: ' + rid + ' gid: ' + str(gid)
                break

    def login_server(self, server_ip, server_port):
        data = {'ip': server_ip, 'port': server_port, 'room': self.roomid}
        self.groupid = int(requests.post(LOGIN_SERVER, data=data).text)
        print self.groupid
        pass
