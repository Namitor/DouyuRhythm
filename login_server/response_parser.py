import re

__author__ = 'wangzi6147'


def parse_room_id(html):
    return re.search(r'"room_id":(\d*)', html).group(1)


def parse_server_info(html):
    match = re.search(r'%7B%22ip%22%3A%22(.*?)%22%2C%22port%22%3A%22(.*?)%22%7D%2C', html)
    return match.group(1), match.group(2)


def parse_id(response):
    match = re.search(r'type@=setmsggroup.*/rid@=(\d*?)/gid@=(\d*?)/', response)
    if match == None:
        return '', -1
    else:
        return match.group(1), int(match.group(2))


def parse_content(msg):
    match = re.search(r'type@=chatmessage/.*/sender@=(\d.*?)/content@=(.*?)/snick@=(.*?)/', msg)
    if match == None:
        return -1, '', ''
    else:
        return match.group(1), match.group(3), match.group(2)
