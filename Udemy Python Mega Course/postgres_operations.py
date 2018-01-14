import psycopg2


def connect_database(connectionstring):
    return psycopg2.connect(connectionstring)


def close_database(connection):
    connection.close()


def create_table(connection, table, schema):
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS " + table + " (" + schema + ")")
    connection.commit()


def insert_data(connection, table, item, quantity, price):
    cur = connection.cursor()
    # cur.execute("INSERT INTO %s VALUES('%s','%s','%s')" % (table, item, quantity, price))
    # using %s instead of '%s' to prevent sql injection
    cur.execute("INSERT INTO " + table + " VALUES(%s,%s,%s)", (item, quantity, price))

    connection.commit()


def delete_item(connection, table, item):
    cur = connection.cursor()
    cur.execute("DELETE FROM " + table + " WHERE item=%s", (item,))
    connection.commit()


def update_item(connection, table, item, quantity, price):
    cur = connection.cursor()
    cur.execute("UPDATE " + table + " SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    connection.commit()


def read_data(connection, table):
    cur = connection.cursor()
    cur.execute("SELECT * FROM " + table)
    return cur.fetchall()


connection_string = "dbname='udemy1' user='postgres' password='Test1234' host='localhost' port='5432'"
table = 'vine_store'
schema = 'item TEXT, quantity INTEGER, price REAL'

conn = connect_database(connection_string)

# create_table(conn, table, schema)

# insert_data(conn, table, 'Chardonay', 789, 6.59)
# insert_data(conn, table, 'Malbec', 567, 8.99)
# insert_data(conn, table, 'Tokay', 234, 4.79)

update_item(conn, table, 'Merlot', 0, 3.99)

print(read_data(conn, table))

close_database(conn)
