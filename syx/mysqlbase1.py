#coding=utf-8
import MySQLdb
import datetime

conn = MySQLdb.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = 'root',
    db = 'monitor',
)
cur = conn.cursor() #游标
#cur.execute("insert into monitor.process_log (processname,created_time) VALUES ('dpo_001.py',now())")
#now = datetime.datetime.now()
#print now
sqli="select * from process_log "

for dates in cur.fetchmany(cur.execute(sqli)):
    print dates
#conn.commit() #提交事务，插入,修改必须使用这个命令
cur.close()