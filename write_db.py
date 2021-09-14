import pymysql
import re
# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')

# 获取游标（操作sql语句）
cur = db.cursor()
f = open("dict.txt", "r")


    # 写入操作
sql = 'insert into words (name,explan) values (%s,%s);'
for line in f:
    #获取单词和解释
    tup=re.findall(r"(\S+)\s+(.*)",line)[0]
    try:
        cur.execute(sql,tup)
        db.commit()
    except Exception as e:
        db.rollback()#报错返回上上一个数据库形态，防止损害数据
        print(e)
f.close()
#关闭数据库
cur.close()
db.close()
