import sqlite3


def connect_database(database):
    return sqlite3.connect(database)


def close_database(connection):
    connection.close()


def create_table(connection, table, schema):
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS " + table + " (" + schema + ")")
    connection.commit()


def insert_data(connection, table, item, quantity, price):
    cur = connection.cursor()
    cur.execute("INSERT INTO " + table + " VALUES(?,?,?)", (item, quantity, price))
    # using ? instead of %s to prevent sql injection
    connection.commit()


def delete_item(connection, table, item):
    cur = connection.cursor()
    cur.execute("DELETE FROM " + table + " WHERE item=?", item)
    connection.commit()


def update_item(connection, table, item, quantity, price):
    cur = connection.cursor()
    cur.execute("UPDATE " + table + "SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    connection.commit()


def read_data(connection, table):
    cur = connection.cursor()
    cur.execute("SELECT * FROM " + table)
    return cur.fetchall()


db = 'files\lite.db'
table = 'vine_store'
schema = 'item TEXT, quantity INTEGER, price REAL'

conn = connect_database(db)

create_table(conn, table, schema)

insert_data(conn, table, 'Merlot', 1002, 4.99)
insert_data(conn, table, 'Shiraz', 547, 7.99)
insert_data(conn, table, 'Cabernet', 798, 6.99)

print(read_data(conn, table))

close_database(conn)
