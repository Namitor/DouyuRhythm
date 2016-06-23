# coding=utf-8
__author__ = 'jayvee'

import logging
from logging.handlers import RotatingFileHandler
import os

# 用以控制是否输出到屏幕，线上环境不输出到屏幕
DebugConf = True
# DebugConf = False

abs_path = os.path.dirname(os.path.abspath(__file__))
abs_father_path = os.path.dirname(abs_path)
log_dir_path = abs_father_path + '/log'
if not os.path.exists(log_dir_path):
    os.makedirs(log_dir_path)

common_logger = logging.getLogger('common')
formatter = logging.Formatter('[%(asctime)s][pid:%(process)s] %(module)s.%(funcName)s: %(levelname)s: %(message)s')

# StreamHandler for print log to console
hdr = logging.StreamHandler()
hdr.setFormatter(formatter)
hdr.setLevel(logging.DEBUG)

# RotatingFileHandler
chr_feature = RotatingFileHandler('%s/common.log'%(log_dir_path), maxBytes=10*1024*1024, backupCount=3)
chr_feature.setFormatter(formatter)
chr_feature.setLevel(logging.DEBUG)


common_logger.addHandler(chr_feature)
common_logger.addHandler(hdr)
common_logger.setLevel(logging.DEBUG)
