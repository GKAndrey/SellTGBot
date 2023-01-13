import sqlite3
import os

PATH = os.path.abspath(__file__ + '/..')

con = sqlite3.connect(os.path.join(PATH, "database.db"))

cursor = con.cursor()
adminer = cursor.execute('''
ALTER TABLE users
ADD sends varchar(2);
''')
adminer = adminer.fetchall()
# adminer = cursor.execute("SELECT admin FROM users WHERE id = ?", (1439133134, ))
# adminer = adminer.fetchall()
# print(adminer)
# # cursor.execute("DELETE FROM users WHERE id=?;")
# con.commit()

# add_student_sql = '''
# INSERT INTO students
# VALUES (?,?,?,?,?);
# '''
# add_student_sql = '''
# SELECT * FROM students;
# '''
# result = cursor.execute(add_student_sql)

# print(result.fetchall())
con.commit()