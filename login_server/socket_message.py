__author__ = 'wangzi6147'

import struct


def build(content):
    ct_len = len(content)
    req_len = len(content) + 4 + 4 + 1
    fmt = '<iii' + str(ct_len + 1) + 's'
    bytes = struct.pack(fmt, req_len, req_len, 0x2b1, content)
    return bytes



