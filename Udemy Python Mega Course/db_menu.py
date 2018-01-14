import postgres_oop
import os, msvcrt


def get_menu_option():
    os.system('cls')
    print('-' * 35)
    print('     STORE DATABASE SYSTEM')
    print('-'*35)
    print(' 0  -->  create a new store table')
    print(' 1  -->  select current table')
    print(' 2  -->  insert data to table')
    print(' 3  -->  update data in table')
    print(' 4  -->  delete data from table')
    print(' 5  -->  display table data')
    print(' 6  -->  display tables')
    print('-' * 35)
    print(' Q  -->  exit the system\n')

    return input('what is your action?  ')


def pause():
    nul = input("\n\t\t\tOK, press ENTER to continue...")


connection_string = "dbname='udemy1' user='postgres' password='Test1234' host='localhost' port='5432'"
schema = 'item TEXT, quantity INTEGER, price REAL'
db = postgres_oop.PostgresDB(connection_string)

action = ''
while action.lower() != 'q':
    action = get_menu_option()
    tbl_item = ''
    tbl_qty = ''
    tbl_price = ''
#    try:
    if action == '0':
        tbl_name = ''
        tbl_name = input("enter new table name or press enter to return to menu: ")
        if tbl_name == '':
            pass
        else:
            db.create_table(tbl_name, schema)

    elif action == '1':
        tbl_name = input("enter current table name or press enter to return to menu: ")
        if tbl_name == '':
            pass
        else:
            pause()

    elif action == '2':
        tbl_item = input("enter item name or press enter to return to menu: ")
        tbl_qty = input("enter item quantity or press enter to return to menu: ")
        tbl_price = input("enter item price or press enter to return to menu: ")
        if tbl_item == '' or tbl_item == '' or tbl_qty == '':
            break
        else:
            db.insert_data(tbl_name, tbl_item, tbl_qty, tbl_price)
            pause()

    elif action == '3':
        tbl_item = input("enter item name or press enter to return to menu: ")
        tbl_qty = input("enter item quantity or press enter to return to menu: ")
        tbl_price = input("enter item price or press enter to return to menu: ")
        if tbl_item == '' or tbl_item == '' or tbl_qty == '':
            break
        else:
                db.update_data(tbl_name, tbl_item, tbl_qty, tbl_price)
                pause()

    elif action == '4':
        tbl_item = input("enter item name or press enter to return to menu: ")
        if tbl_name == '':
            break
        else:
                db.delete_item(tbl_name, tbl_item)
                pause()

    elif action == '5':
        if tbl_name == '':
            print('table name not set ')
            pause
        else:
                print(db.read_data(tbl_name))
                pause()

    elif action == '6':
                print(db.get_tables())
                pause()

    else:
        pass

#    except:
#        print('oh no! there was some error, try again')

print('Exiting the system ...')
pause()
os.system('cls')

