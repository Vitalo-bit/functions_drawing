import sqlite3


def user_registration():
    db = sqlite3.connect('accounts.sqlite')
    sql = db.cursor() # work with database

    sql.execute("""CREATE TABLE IF NOT EXISTS users (
        login TEXT, 
        password TEXT 
    )""")

    db.commit()
    user_login = self.nickEdit.text()
    user_password = self.passEdit.text()
    # reg
    sql.execute(f"""SELECT LOGIN FROM users WHERE login = '{user_login}'""")
    if sql.fetchone() is None:
        sql.execute(f"""INSERT INTO users VALUES (?, ?)""", (user_login, user_password))
        db.commit()
        print('Your account is registered')
        return True
    else:
        sql.execute(f"""SELECT LOGIN FROM users WHERE login = '{user_password}'""")
        if sql.fetchone() is None:
            print('Wrong password')
            return False
        else:
            return True
