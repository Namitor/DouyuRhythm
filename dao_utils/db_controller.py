from datetime import datetime
import random
import pymongo

__author__ = 'jayvee'

# mongo
mongo_client = pymongo.MongoClient('115.28.76.209', 27017)
db_main = mongo_client.get_database('ProjectTides')
db_danmu = db_main.get_collection('danmu')


def get_recent_danmu(room_id, db_inst=db_danmu, **kwargs):
    find_result = db_inst.find({"room_id": room_id}).sort('post_time', -1).limit(30)
    return find_result


def save_danmu(userid, user_name, content, post_time, room_id, db_inst=db_danmu):
    db_inst.insert({'userid': userid, 'user_name': user_name, 'content': content, 'post_time': datetime.utcnow(),
                    'room_id': room_id})


if __name__ == '__main__':
    # save_danmu({"msg": 'hahahahahahahah', 'user': 'nimei' + str(random.random()), 'time': datetime.utcnow()})
    for i in get_recent_danmu('67373'):
        print i['content']
