import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
#cursor.execute(create_table)

user = (1, 'antonis', 'azerty')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
  (2, 'rolf', 'qsdf'),
  (3, 'anna', 'wxc')
]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users "
for row in cursor.execute(select_query):
  print(row)

connection.commit()

connection.close()
