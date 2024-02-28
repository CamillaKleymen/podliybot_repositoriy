import sqlite3

connection = sqlite3.connect('podliybot.db', check_same_thread=False)
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS podlie_users ('
            'id INTEGER,'
            'name TEXT, '
            'number TEXT, '
            'location TEXT'
            ');')

sql.execute('CREATE TABLE IF NOT EXISTS menu ('
            'fd_id INTEGER, '
            'fd_name TEXT, '
            'fd_count INTEGER,'
            'fd_contain TEXT,'
            'fd_price REAL'
            ');')


def check_user(fd_id):
    check = sql.execute('SELECT * FROM podlie_users WHERE id=?;', (fd_id,))
    if check.fetchone():
        return True
    else:
        return False


def register(id, name, number, location):
    sql.execute('INSERT INTO podlie_users VALUES(?, ?, ?, ?);', (id, name, number, location))

    connection.commit()

def get_id():
    return sql.execute('SELECT id, name, number, location FROM podliye_users;').fetchall()

def get_fd_id(fd_id):
    return sql.execute('SELECT fd_id, fd_name, fd_count, fd_contain, fd_price' 
                       'FROM menu where fd_id =?;', (fd_id,)).fetchone()

def add_fd_tocart(fd_id, fd_name, fd_count, fd_contain, fd_price):
    sql.execute(' INSERT INTO menu VALUES(?, ?, ?);', (fd_id, fd_name, fd_count, fd_price, fd_contain))
    connection.commit()


#side of admin
def add_fd(fd_id, fd_name, fd_count, fd_contain, fd_fd_price):
    sql.execute('INSERT INTO menu(fd_id, fd_name, fd_count, fd_contain, fd_price)'
                'VALUES(?, ?, ?, ?);', (fd_id, fd_name, fd_count, fd_contain, fd_fd_price))
    connection.commit()

def del_fd(fd_id):
    sql.execute('DELETE FROM menu WHERE fd_id = ?;', (fd_id,))
    connection.commit()

def change_fd_count(fd_id, new_count):
    current_count = sql.execute('SELECT fd_count FROM menu WHERE fd_id=?;', (fd_id,).fetchone()
    sql.execute('UPDATE menu SET fd_count=? WHERE fd_id=?;',
                (current_count[0]+new_count, fd_id))
    connection.commit()

def check_fd():
    fd_check = sql.execute('SELECT * FROM menu;')
    if fd_check.fetchone():
        return True
    else:
        return False

def show_cart(user_id):
    cart_check = sql.execute('SELECT * FROM cart WHERE id=?;', (user_id,))
    if cart_check.fetchone():
        return cart_check.fetchone()
    else:
        return False

def clear_cart(user_id):
    sql.execute('DELETE FROM cart WHERE id=?;', (user_id,))
    connection.commit()


def make_order(user_id):
    fd_name = sql.execute('SELECT user_fd_name FROM cart WHERE id=?;', (user_id,)).fetchone()
    user_fd_count = sql.execute('SELECT user_fd_count FROM cart WHERE id=?;',
                                (user_id,)).fetchone()
    current_count = sql.execute('SELECT pr_count FROM products WHERE fd_name=?;',
                                (fd_name[0],)).fetchone()
    sql.execute('UPDATE products SET fd_count=? WHERE fd_name=?;',
                (current_count[0]-user_fd_count[0], fd_name[0]))
    info = sql.execute('SELECT * FROM cart WHERE id=?;', (user_id,)).fetchone()
    address = sql.execute('SELECT location FROM users WHERE id=?;', (user_id,)).fetchone()
    sql.execute('DELETE FROM cart WHERE id=?;', (user_id,))
    connection.commit()
    return info, address




















