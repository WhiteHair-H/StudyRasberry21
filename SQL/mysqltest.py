import MySQLdb

# ip(domain), userid , password , database , 한글 사용할때는 utf8
db = MySQLdb.connect('localhost', 'root', '12345', 'test', charset='utf8')
cur = db.cursor(MySQLdb.cursors.DictCursor)

# insert 구문
cur.execute("INSERT INTO student VALUES ({0},'{1}','{2}')".format(3,'FullName', '1987-09-21'))

# commit 필수
db.commit() 

# select 구문
cur.execute('SELECT * FROM student')

while True:
    student = cur.fetchone() # 커서를 한줄씩 읽음
    if not student: break

    print(student)



cur.close()
db.close()
