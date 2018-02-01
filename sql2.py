import pymysql
db = pymysql.connect(host='192.168.33.30',user='root',password='root',db='test',port=3306)

cur = db.cursor()
sql_insert = "insert into user(name,url) values('test','test.com')"
try:
    affected_rows = cur.execute(sql_insert)
    db.commit()
    print(cur.lastrowid)
except Exception as e:
    print(e)
finally:
    db.close()
