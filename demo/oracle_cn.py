import cx_Oracle
host=''
port=''
side=''
user=''
password=''
desc='{}:{}/{}'.format(host,port,side)
db=cx_Oracle.connect(user,password,desc)
sql=''

try:
    cr=db.cursor()  #创建游标
    cr.execute(sql)
    db.commit()
except Exception as e:
    print('connect error:',e)
finally:
    db.close

