from datetime import datetime
import random
import pymongo

__author__ = 'jayvee'

# mongo
mongo_client = pymongo.MongoClient('115.28.76.209', 27017)
db_main = mongo_client.get_database('ProjectTides')
db_danmu = db_main.get_collection('danmu')


# db_refinedlog.authenticate('senzhub', 'Senz2everyone')
# db_user_location = db_refinedlog.get_collection('UserLocation')
# db_user_motion = db_refinedlog.get_collection('UserMotion')
# db_hos = db_refinedlog.get_collection('HomeOfficeStatus')
# db_combined_timeline = db_refinedlog.get_collection('CombinedTimelines')


def get_danmu(db_inst=db_danmu):
    find_result = db_inst.find({'tag': 'test_data'})
    return find_result


def save_danmu(user_name, content, post_time, room_id, db_inst=db_danmu):
    db_inst.insert({'user_name': user_name, 'content': content, 'post_time': datetime.utcnow(), 'room_id': room_id})


if __name__ == '__main__':
    save_danmu({"msg": 'hahahahahahahah', 'user': 'nimei' + str(random.random()), 'time': datetime.utcnow()})
    for i in get_danmu():
        print i
