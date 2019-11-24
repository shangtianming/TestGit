import pymysql
# 打开数据库连接
db=pymysql.connect('localhost','root','yinwenbin','yin_test')
# 创建游标对象
cs=db.cursor()
# 使用 execute() 方法执行 SQL，如果表存在则删除
cs.execute('drop table if exists people')
sql='create table people (\
	 id int primary key not null auto_increment,\
	 country varchar(20) not null,\
	 population int(20)not null,\
	 createtime datetime DEFAULT CURRENT_TIMESTAMP,\
	 updatetime datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP )'
cs.execute(sql)
# SQL 插入语句
s1="insert into people (country,population)values('中国',600)"
try:
	cs.execute(s1)# 执行sql语句
	db.commit()# 提交到数据库
except:
	print('+-+-+')
	db.rollback()# 如果发生错误则回滚
# 关闭数据库连接

db.close()