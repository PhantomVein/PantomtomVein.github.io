import MySQLdb

db = MySQLdb.connect(host='127.0.0.1',  # 
                                  port=3306, 
                                  db='github', 
                                  user='root', 
                                  passwd='szt998505', 
                                  charset='utf8', 
                                  use_unicode=True)
cursor = db.cursor()
sql = """select stargazers_count FROM repositories order by stargazers_count  desc"""
cursor.execute(sql)
f = open("repo_name.txt", "w")
k = 1
for info in cursor.fetchall():  
    f.write("[")
    f.write(str(k))
    f.write(",")
    f.write(str(info[0]))
    f.write("],")
    k+=1
f.close()
cursor.close()
db.close()