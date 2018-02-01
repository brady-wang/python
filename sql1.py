import pymysql
#建立连接
db = pymysql.connect(host = '192.168.33.30', user='root', password='root',db='test',port=3306)
#获取只游标 
cur = db.cursor()

sql = 'select * from user'

try:
    cur.execute(sql)
    result = cur.fetchall()
    for res in result:
        id = res[0]
        name=res[1]
        url=res[2]
        print("id= %s name= %s url = %s" %(id,name,url))
except Exception as e:
    print(e)
finally:
    db.close()