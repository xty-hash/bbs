import pymysql
# 建库
conn = pymysql.Connect(host = '127.0.0.1',user='root',
                       password='123',
                       port=3306,charset='utf8')
cursor = conn.cursor()
sql = "create database bbs default charset=utf8"

cursor.execute(sql)

conn.close()
cursor.close()
# 建表
conn = pymysql.Connect(host = '127.0.0.1',user='root',
                       password='123',db='bbs',
                       port=3306,charset='utf8')
cursor = conn.cursor()
sql = "create table if not exists user(uid int primary key auto_increment,username varchar(100) unique,usertype enum('0','1') default '0',password varchar(200),regtime datetime,email varchar(200))"

cursor.execute(sql)

conn.close()
cursor.close()

# 用户注册
conn = pymysql.Connect(host='127.0.0.1', user='root',
                           password='123',
                           db='bbs', port=3306, charset='utf8')

cursor = conn.cursor()
try:
    username = input("输入名字")
    password = input("输入密码")

    sql1 = "insert into user(username,password) values ('{}','{}')".format(username,password)
    sql2 = "select username from user"

    cursor.execute(sql1)
    cursor.execute(sql2)
    conn.commit()

    if len(username) > 2 and username not in sql2:
        print("注册成功")
    else:
        print("重新注册")

except Exception as e:
    print(e)
    conn.rollback()

finally:
    conn.close()
    cursor.close()

# 用户登录
from hashlib import sha1
conn = pymysql.Connect(host='127.0.0.1', user='root',
                           password='123',
                           db='bbs', port=3306, charset='utf8')

cursor = conn.cursor()

username = input("输入名字")
password = input("输入密码")
# password = sha1(password.encode('utf8')).hexdigest()

sql3 = "select username password from user where username=%s and password=%s"

result = cursor.execute(sql3,[username,password])
#
if result > 0:
    print("登陆成功")
else:
    print("登录失败")

conn.close()
cursor.close()

# 显示
conn = pymysql.Connect(host='127.0.0.1', user='root',
                           password='123',
                           db='bbs', port=3306, charset='utf8')

cursor = conn.cursor()
sql4 = 'select * from user'

try:
    cursor.execute(sql4)

    data = cursor.fetchall()
    print(data)
except Exception as e:
    print(e)
finally:
    cursor.close()
    conn.close()

































