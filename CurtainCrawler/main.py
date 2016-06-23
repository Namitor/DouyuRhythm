# coding=utf-8
import threading
import time

from Crawler import Crawler
# from dao_utils import db_controller
from home_page.crawler_monitor import OverWatcher

__author__ = 'wangzi6147'


def main():
    crawler1 = Crawler('http://www.douyu.com/97376', '1')
    crawler2 = Crawler('http://www.douyu.com/4809', '2')
    crawler3 = Crawler('http://www.douyu.com/chuan967', '3')
    ow = OverWatcher()
    ow.add_task(crawler1)
    print ow.show_all_task()
    time.sleep(5)
    ow.add_task(crawler2)
    print ow.show_all_task()
    time.sleep(5)
    ow.add_task(crawler3)
    print ow.show_all_task()
    print 'stard done'
    time.sleep(5)
    ow.remove_task('1')
    print ow.show_all_task()
    time.sleep(5)
    ow.remove_task('2')
    print ow.show_all_task()
    time.sleep(5)
    # ow.remove_task('3')
    print ow.show_all_task()
    print 'stoped'
    # for userid, nickname, content, post_time, room_id in crawler.start():
    #     print '[%s]%s: %s' % (post_time, nickname, content)
    #     db_controller.save_danmu(userid, nickname, content, post_time, room_id)


if __name__ == '__main__':
    main()
