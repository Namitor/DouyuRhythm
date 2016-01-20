from Crawler import Crawler
from dao_utils import db_controller

__author__ = 'wangzi6147'


def main():
    crawler = Crawler()
    for userid, nickname, content, post_time, room_id in crawler.start('http://www.douyutv.com/qiuri'):
        print '[%s]%s: %s' % (post_time, nickname, content)
        db_controller.save_danmu(userid, nickname, content, post_time, room_id)


if __name__ == '__main__':
    main()
