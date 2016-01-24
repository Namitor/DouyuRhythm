# coding=utf-8
import socket, time, uuid, hashlib, socket_message, response_parser
from flask import Flask, request

__author__ = 'wangzi6147'

app = Flask(__name__)
HOST = '0.0.0.0'
PORT = 9090


@app.route('/login', methods=['POST'])
def login():
    print 'req'
    gid = -1
    douyu_login_ip = request.form['ip']
    douyu_login_port = request.form['port']
    douyu_room_id = request.form['room']
    douyu_login_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    douyu_login_socket.connect((douyu_login_ip, int(douyu_login_port)))
    cur_time = str(int(time.time()))
    devid = str(uuid.uuid1()).replace('-', '').upper()
    m = hashlib.md5()
    m.update(str(cur_time) + '7oE9nPEG9xXV69phU31FYCLUagKeYtsF' + devid)
    vk = m.hexdigest()
    douyu_login_socket.send(socket_message.build(
        'type@=loginreq/username@=/ct@=0/password@=/roomid@={0}/devid@={1}/rt@={2}/vk@={3}/ver@=20150929/'.format(
            douyu_room_id, devid, cur_time, vk)))
    while 1:
        response = douyu_login_socket.recv(1024)
        rid, gid = response_parser.parse_id(response)
        if rid != '' and gid != -1:
            print 'rid: ' + rid + ' gid: ' + str(gid)
            break
    douyu_login_socket.close()
    return str(gid)


if __name__ == '__main__':
    app.run(HOST, port=PORT, debug=True)
