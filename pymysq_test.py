# @Time : 2021/4/12 18:27 
# @Author : Smile_Mr
# @File : pymysq_test.py 
# @Software: PyCharm
import pymysql

def del_pymysql(userid_list):

    db = pymysql.connect("127.0.0.1",'user','password','common_service')
    cursor = db.cursor()
    try:
        sql = "delete from user_profile_data_0 where userId='%s';"
        cursor.execute(sql,userid_list)
        db.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()

if __name__ == '__main__':

    userid_list = []
    del_pymysql(userid_list)