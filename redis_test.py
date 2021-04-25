# @Time : 2021/4/12 18:35 
# @Author : Smile_Mr
# @File : redis_test.py 
# @Software: PyCharm
import redis
def del_redis(userid,db):

    try:
        pool=redis.ConnectionPool(host='192.168.1.126',port=6379,db=db)
        r = redis.StrictRedis(connection_pool=pool)
        r.delete('common-service:userProfileData:%s'%userid)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    userid = ''
    for i in range(1,11):
        del_redis(userid,i)