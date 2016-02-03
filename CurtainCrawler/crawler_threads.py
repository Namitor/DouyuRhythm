# coding=utf-8
import os
import threading
import sys
import time

project_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_path)
print 'project path = %s' % project_path

from CurtainCrawler.Crawler import Crawler

__author__ = 'jayvee'

task_dict = {}


# class CrawlerThread(threading.Thread):
#     def __init__(self, room_url):
#         threading.Thread.__init__(self)
#         self.is_stop = False
#         self.room_url = room_url
#
#     def run(self):
#         # TODO 这里的爬取线程应该封装一下，目前的跳转太多了，Crawler类里面的start()函数，启动了一个HeartBeat线程，自己又来了个while true
#         # 目前的想法是，重新设计一下crawler类，分析一下有多少需要开的线程（heartbeat需要每个房间都开一个？），然后在关键的地方，设计一个停止函数
#         # task dict存储房间的爬取线程实例，有一个函数来控制线程的停止，参考下面的stop_crawl_room
#         crawl_and_save(self.room_url, self.is_stop)
#
#     def set_stop(self):
#         print '%s stop' % self.room_url
#         self.is_stop = True
#
#
# def crawl_and_save(room_url, is_stop):
#     crawler = Crawler(room_url)
#     print 'start crawl %s' % room_url
#     crawler.start()
#     # thread.start_new_thread(crawler.start, ())
#     # for userid, nickname, content, post_time, room_id in crawler.start():
#     #     print '[room:%s][%s]%s: %s' % (room_id, post_time, nickname, content)
#     #     db_controller.save_danmu(userid, nickname, content, post_time, room_id)


def start_crawl_room_list(room_urls):
    # task_list =[]
    for room_url in room_urls:
        # thread.start_new_thread(crawl_and_save, (room_url,))
        # task_list.append(gevent.spawn(crawl_and_save, room_url))
        crawler_task = Crawler(room_url)
        # crawler_task.run()
        # thread_task = threading.Thread(target=crawl_and_save, name=room_url, args=(room_url,))
        task_dict[room_url] = crawler_task
        crawler_task.start()
    print 'start tasks'
    # gevent.joinall(task_list)
    # print 'tasks done'


def stop_crawl_room(room_url):
    if task_dict.get(room_url):
        room_task = task_dict[room_url]
        room_task.stop()


if __name__ == '__main__':
    room_url_list = ['http://www.douyutv.com/weixiao',
                     'http://www.douyutv.com/cave',
                     'http://www.douyutv.com/pis']
    start_crawl_room_list(room_url_list)

    time.sleep(5)
    task_dict['http://www.douyutv.com/weixiao'].stop()
    time.sleep(5)
    task_dict['http://www.douyutv.com/cave'].stop()
    time.sleep(5)
    task_dict['http://www.douyutv.com/pis'].stop()
