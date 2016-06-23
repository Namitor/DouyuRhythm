from common_utils.logging_utils import common_logger

__author__ = 'jayvee'


class OverWatcher(object):
    def __init__(self):
        self.running_tasks = {}

    def add_task(self, crawler_thread):
        common_logger.info('add task: %s' % crawler_thread.thread_id)
        self.running_tasks[crawler_thread.thread_id] = crawler_thread
        crawler_thread.start()

    def remove_task(self, crawler_id):
        crawler_thread = self.running_tasks.get(crawler_id, None)
        if crawler_thread:
            crawler_thread.shutdown()
            del self.running_tasks[crawler_id]
        else:
            common_logger.error('no crawler named %s' % crawler_id)

    def show_all_task(self):
        res = []
        for v in self.running_tasks.values():
            res.append(v.url)
        return res
