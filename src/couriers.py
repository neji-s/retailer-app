def courier_menu():
    print()
    print('0. Return to Main Menu')
    print('1. Show Courier List')
    print('2. Create New Courier')
    print('3. Update Existing Courier')
    print('4. Delete Courier')
    print()
    
def show_courier_list(db_cursor):
    sql_select_query = 'select * from couriers'
    db_cursor.execute(sql_select_query)
    rows = db_cursor.fetchall()
    for row in rows:
        for col in row:
            print(col,end=' ')
        print()

def create_new_courier(db_cursor,db_connection):
    new_cour_name = input('Please enter new courier name: ')
    new_cour_phone = input('Please enter new courier phone number: ')
    sql = 'INSERT INTO couriers (courier_name, courier_phone) VALUES (%s, %s)' 
    val = (new_cour_name, new_cour_phone)
    db_cursor.execute(sql,val)
    db_connection.commit()
    print()
    print(db_cursor.rowcount, "Record inserted successfully into courier table")

def update_courier(db_cursor,db_connection):
    chng_cour = int(input(f'\nPlease select the number of which courier you want to update: '))
    upd_name = input('Please enter new courier name: ')
    upd_phone = float(input('Please enter new courier phone number: '))
    sql = f"UPDATE couriers SET courier_name = %s, courier_phone = %s WHERE courier_id = %s"
    val = (upd_name, upd_phone, chng_cour)
    db_cursor.execute(sql, val)
    db_connection.commit()
    print()
    print(f'Courier {chng_cour} updated successfully')
    
def delete_courier(db_cursor,db_connection):
    del_cour = int(input('Please enter the index of the courier you wish to delete: '))
    sql = f'DELETE FROM couriers WHERE courier_id = {del_cour}'
    db_cursor.execute(sql)
    db_connection.commit()
    print()
    print(f'Courier {del_cour} successfully deleted')