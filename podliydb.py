import sqlite3

connection = sqlite3.connect('podliybot.db', check_same_thread=False)
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS podlie_users ('
            'id INTEGER,'
            'name TEXT, '
            'number TEXT, '
            'location TEXT'
            ');')

sql.execute('CREATE TABLE IF NOT EXISTS usergroup ('
            'id INTEGER, '
            'user_pr_name TEXT, '
            'user_pr_count INTEGER'
            ');')

def check_user(id):
    check = sql.execute('SELECT * FROM podlie_users WHERE id=?;', (id,))
    if check.fetchone():
        return True
    else:
        return False

def register(id, name, number, location):
    sql.execute('INSERT INTO podliye_users VALUES(?, ?, ?, ?);', (id, name, number, location))

    connection.commit()