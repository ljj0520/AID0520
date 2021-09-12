import pymysql

db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='stu',
                   charset='utf8')

cur=db.cursor()

sql="select * from class where sex='男';"

cur.execute(sql)

get_data=cur.fetchall()
print(get_data)

cur.close()
db.close()
