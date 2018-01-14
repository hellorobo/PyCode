import psycopg2


class PostgresDB:

    def __init__(self, connstr):
        self.connection = psycopg2.connect(connstr)
        self.cur = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def create_table(self, table, schema):
        self.cur.execute("CREATE TABLE IF NOT EXISTS " + table + " (" + schema + ")")
        self.connection.commit()

    def insert_data(self, table, item, quantity, price):
        self.cur.execute("INSERT INTO " + table + " VALUES(%s,%s,%s)", (item, quantity, price))
        self.connection.commit()

    def delete_item(self, table, item):
        self.cur.execute("DELETE FROM " + table + " WHERE item=%s", (item,))
        self.connection.commit()

    def update_item(self, table, item, quantity, price):
        self.cur.execute("UPDATE " + table + " SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
        self.connection.commit()

    def read_data(self, table):
        self.cur.execute("SELECT * FROM " + table)
        return self.cur.fetchall()

    def get_tables(self):
        rv = []
        tables = self.cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
        for t in tables.fetchall():
            rv.append(t)
        return rv


connection_string = "dbname='udemy1' user='postgres' password='Test1234' host='localhost' port='5432'"
db = PostgresDB(connection_string)

"""
db.create_table('book_store', 'item TEXT, quantity INTEGER, price REAL')

table = 'book_store'

db.insert_data(table, 'Inferno', 78, 6.59)
db.insert_data(table, 'Bible', 56, 8.99)
db.insert_data(table, 'Makbet', 23, 4.79)

db.update_item(table, 'Makbet', 0, 6.99)

print(db.read_data(table))

"""