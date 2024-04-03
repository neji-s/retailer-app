def prod_menu():
    print()    
    print('0. Return to Main Menu')
    print('1. Show Product List')
    print('2. Create New Product')
    print('3. Update Existing Product')
    print('4. Delete Product')
    print()

# obtains data from sql products table and presents this to user in a list type format. db_cursor is a placeholder for the cursor global variable. same logic is used for courier, order and order status lists below.
def show_prod_list(db_cursor):
    sql_select_query = 'select * from products'
    db_cursor.execute(sql_select_query)
    rows = db_cursor.fetchall()
    for row in rows:
        for col in row:
            print(col,end=' ')
        print()

def create_new_product(db_cursor,db_connection):
    new_prod_name = input('Please enter new product name: ')
    new_prod_price = input('Please enter new product price: ')
    sql = 'INSERT INTO products (product_name, product_price) VALUES (%s, %s)' 
    val = (new_prod_name, new_prod_price)
    db_cursor.execute(sql,val)
    db_connection.commit()
    print(db_cursor.rowcount, "Record inserted successfully into products table")
    
def update_product(db_cursor,db_connection):
    chng_prod = int(input(f'\nPlease select the number of which product you want to update: '))
    upd_name = input('Please enter new product name: ')
    upd_price = float(input('Please enter new product price: '))
    sql = f"UPDATE products SET product_name = %s, product_price = %s WHERE product_id = %s"
    val = (upd_name, upd_price, chng_prod)
    db_cursor.execute(sql, val)
    db_connection.commit()
    print(f'\nProduct {chng_prod} updated successfully')

def delete_product(db_cursor,db_connection):
    del_prod = int(input('Please enter the index of the product you wish to delete: '))
    sql = f'DELETE FROM products WHERE product_id = {del_prod}'
    db_cursor.execute(sql)
    db_connection.commit()
    print()
    print(db_cursor.rowcount, "Record inserted deleted from products table")
                   