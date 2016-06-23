# coding=utf-8
import threading
import time

from Crawler import Crawler
# from dao_utils import db_controller

__author__ = 'wangzi6147'


def main():
    crawler = Crawler('http://www.douyu.com/97376')
    crawler.start()
    # crawler.join()
    time.sleep(10)
    crawler.shutdown()
    crawler.join()
    print 'stoped'
    # for userid, nickname, content, post_time, room_id in crawler.start():
    #     print '[%s]%s: %s' % (post_time, nickname, content)
    #     db_controller.save_danmu(userid, nickname, content, post_time, room_id)


if __name__ == '__main__':
    main()
