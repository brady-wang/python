import pymysql
db = pymysql.connect(host='192.168.33.30',user='root',password='root',db='test',port=3306)
cur = db.cursor()

sql_del = "delete from user where id = %d"

try:
    cur.execute(sql_del %(1))
    db.commit()
except Exception as e:
    db.rollback()
finally:
    db.close()