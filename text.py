import pymysql
#链接数据库
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='stu',
                   charset='utf8')
#获取游标（操作数据库，执行sql语句）
cur=db.cursor()

#sql语句
sql="insert into class values (6,'张国荣',25,'男',95);"

cur.execute(sql)#执行sql语句

db.commit()#将写操作提交，多次写一同提交

#关闭数据库
cur.close()
db.close()

