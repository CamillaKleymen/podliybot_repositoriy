import sqlite3

connection = sqlite3.connect('podliybot.db', check_same_thread=False)
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS podlie_users ('
            'id INTEGER,'
            'name TEXT, '
            'number TEXT, '
            'location TEXT,'
            'datereg REAL'
            ');')

sql.execute('CREATE TABLE IF NOT EXISTS usergroups ('
            'gr_id INTEGER, '
            'usergr_name TEXT, '
            'users_count INTEGER'
            'cr_date REAL'
            ');')


def check_user(gr_id):
    check = sql.execute('SELECT * FROM podlie_users WHERE id=?;', (gr_id,))
    if check.fetchone():
        return True
    else:
        return False


def register(id, name, number, location):
    sql.execute('INSERT INTO podlie_users VALUES(?, ?, ?, ?);', (id, name, number, location))

    connection.commit()

def get_user():
    return sql.execute('SELECT id, usergr_name, users_count, cr_date FROM podlie_users;').fetchall()

def get_ex_gr(gr_id):
    return sql.execute('SELECT gr_id, usergr_name, users_count' 
                       'FROM usergroups where gr_id =?;', (gr_id,)).fetchone()

def add_us_ingroup(user_id, user_name, user_gr):
    sql.execute(' INSERT INTO podlie_users VALUES(?, ?, ?);', (user_id, user_name, user_gr))
    connection.commit()

def add_us(gr_id, usergr_name, users_count, cr_date):
    sql.execute('INSERT INTO usergroups(gr_id, usergr_name, users_count, cr_date)'
                'VALUES(?, ?, ?, ?);', (gr_id, usergr_name, users_count, cr_date))
    connection.commit()

def del_gr(gr_id):
    sql.execute('DELETE FROM usergroups WHERE gr_id = ?;', (gr_id,))
    connection.commit()

def check_gr():
    gr_check = sql.execute('SELECT * FROM usergroups;')
    if gr_check.fetchone():
        return True
    else:
        return False























