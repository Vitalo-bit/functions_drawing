import sqlite3

db = sqlite3.connect('accounts.sqlite')
sql = db.cursor()  # work with database

user_login = '1234'
user_password = '051627'
sql.execute(f"""UPDATE users SET password = '{user_password}' WHERE login = '{user_login}'""")
db.commit()
