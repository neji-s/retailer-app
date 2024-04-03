def orders_menu():
    print()
    print('0. Return to Main Menu')
    print('1. Print Orders List')
    print('2. Create New Order')
    print('3. Update Order Status')
    print('4. Update Existing Order')
    print('5. Delete Order')
    print()

def show_order_list(db_cursor):
    sql_select_query = 'select * from orders'
    db_cursor.execute(sql_select_query)
    rows = db_cursor.fetchall()
    for row in rows:
        for col in row:
            print(col,end=' ')
        print()
        
def show_order_status_list(db_cursor):
    sql_select_query = 'select * from order_status'
    db_cursor.execute(sql_select_query)
    rows = db_cursor.fetchall()
    for row in rows:
        for col in row:
            print(col,end=' ')
        print()

# for readability purposes, i have used an inner join of both orders and order status tables. this function shows only the order id, and the actual order status rather than another id
def show_order_status(db_cursor):
    sql_select_query = 'SELECT order_id, order_status FROM orders INNER JOIN order_status ON orders.order_status_id = order_status.order_status_id'
    db_cursor.execute(sql_select_query)
    rows = db_cursor.fetchall()
    for row in rows:
        for col in row:
            print(col,end=' ')
        print()

def delete_order(db_cursor,db_connection):
    del_ord = int(input('Please enter the index of the order you wish to delete: '))
    sql = f'DELETE FROM orders WHERE order_id = {del_ord}'
    db_cursor.execute(sql)
    db_connection.commit()
    print()
    print(f'Order {del_ord} successfully deleted')
    print()