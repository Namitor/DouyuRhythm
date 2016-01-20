import threading
from CurtainCrawler.Crawler import Crawler

__author__ = 'jayvee'


def crawl_and_save(room_url):
    crawler = Crawler(room_url)
    print 'start crawl %s' % room_url
    crawler.start()
    # thread.start_new_thread(crawler.start, ())
    # for userid, nickname, content, post_time, room_id in crawler.start():
    #     print '[room:%s][%s]%s: %s' % (room_id, post_time, nickname, content)
    #     db_controller.save_danmu(userid, nickname, content, post_time, room_id)


def start_crawl_room_list(room_urls):
    for room_url in room_urls:
        # thread.start_new_thread(crawl_and_save, (room_url,))
        # task_list.append(gevent.spawn(crawl_and_save, room_url))
        thread_task = threading.Thread(target=crawl_and_save, name=room_url, args=(room_url,))
        thread_task.start()
    print 'start tasks'
    # gevent.joinall(task_list)
    # print 'tasks done'


if __name__ == '__main__':
    room_url_list = ['http://www.douyutv.com/67373',
                     'http://www.douyutv.com/71017',
                     'http://www.douyutv.com/qiuri',
                     'http://www.douyutv.com/58428']
    start_crawl_room_list(room_url_list)
