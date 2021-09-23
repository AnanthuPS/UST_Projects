#Pgm for database status

import MySQLdb as mysql

db = mysql.connect(host='localhost', user='root',password='root', db="INFORMATION_SCHEMA")
cur = db.cursor()
cur.execute('SHOW STATUS')
res = cur.fetchall()
res = dict(res)
# print(res)
print("\n")
print("###################################")
print(f"#  Uptime --->>> {res['Uptime']}             #")
print(f"#  Threads_connected --->>> {res['Threads_connected']}     #")
print(f"#  Threads_created --->>> {res['Threads_created']}       #")
print(f"#  Threads_running --->>> {res['Threads_running']}       #")
print(f"#  Queries --->>> {res['Queries']}              #")
print(f"#  Max_used_connections --->>> {res['Max_used_connections']}  #")
print("###################################")
print("\n")
print("---------------PROCESS LIST TABLE---------------")
cur.execute("select * from PROCESSLIST") 
res2 = cur.fetchall()
[print(f"USER ID -> {i[0]} | USER NAME -> {i[1]} | HOST NAME -> {i[2]} | DATABASE -> {i[3]} | COMMAND -> {i[4]} | TIME -> {i[5]} | STATE -> {i[6]} | INFO -> {i[7]}") for i in res2 ]

db.close()