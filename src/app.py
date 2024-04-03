from products import *
from couriers import *
from orders import *
from open import open_app
import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")


connection = mysql.connector.connect(
    host=host_name,
    database=database_name,
    user=user_name,
    password=user_password)

cursor = connection.cursor()
    

def main_menu():
    print('\nMain Menu:')
    print('0. Exit App')
    print('1. Product Menu')
    print('2. Couriers Menu')
    print('3. Orders Menu\n')


print("\nWelcome to the Swift Outlet Management App!")

open_app(cursor, connection)

while True:
    main_menu()
    
    option = input(f'Please Select Option 0, 1, 2 or 3: ')
   
    option = option.strip()
    
    if option == '0':
        print('\nThank you for using the Swift Outlet Management App. Goodbye!\n')
        if connection.is_connected():
            connection.close()
        break
 
    # product menu
    if option == '1':
        while True:
            prod_menu()
                
            option2 = input('Please Select Option 0-4: ')
            option2 = option2.strip()

            if option2 == '0':
                print()
                print('Returning to Main Menu')
                break
                        
            # this will show current product list
            elif option2 == '1':
                show_prod_list(cursor)
                    
            # this will create a new product and add it to the product list, then print the updated list
            elif option2 == '2':
                create_new_product(cursor,connection)
                show_prod_list(cursor)

            # this will show the products with a corresponding index. user enters which product they want to update and are then prompted to update name and/or price
            elif option2 == '3':
                while True:
                    show_prod_list(cursor)
                    update_product(cursor,connection)
                    break
                
            # this will again show a product list, user simply types the product they wish to delete and the product will be deleted. updated list will print         
            elif option2 == '4':
                show_prod_list(cursor)
                delete_product(cursor,connection)
        
            # if user input isnt one of the listed options, an error message is printed and user is taken back to product menu options
            else:
                print('Error')
                print('Please select a valid product menu option')
                         
    # courier menu
    if option == '2':
        while True:
            courier_menu()

            cour_option = input('Please select option 0-4: ')
            cour_option = cour_option.strip()
            
            if cour_option == '0':
                print('\nReturning to Main Menu\n')
                break
            
            # 1 will print current courier list
            if cour_option == '1':
                show_courier_list(cursor)
                
            # this will create a new courier entry and add it to the courier table with a confirmation message
            elif cour_option == '2':
                create_new_courier(cursor,connection)
                show_courier_list(cursor)

            # 3 will update an existing courier. gets user inputs for which courier they want to update, then asks which element they want to update
            elif cour_option == '3':
                while True:
                    show_courier_list(cursor)
                    update_courier(cursor,connection)
                    break
                
            # 4 to delete courier. user input for which courier they want to delete, this is then removed from couriers table
            elif cour_option == '4':
                show_courier_list(cursor)
                delete_courier(cursor,connection)
                show_courier_list(cursor)
                                
            # if user input isnt one of the listed options, an error message is printed and user is taken back to courier menu options
            else:
                print('Error')
                print('Please select a valid courier menu option')
                
    # order menu
    if option == '3':
        while True:
            orders_menu()

            ord_option = input('Please select option 0-5: ')
            ord_option = ord_option.strip()
            
            # using break, will break out of orders menu loop and return to main menu loop
            if ord_option == '0':
                print('Returning to Main Menu')
                break
            
            # 1 will print order list containing dicts of all orders
            elif ord_option == '1':
                show_order_list(cursor)
                
            # 2 will create a new order. we get user input for name, address and phone number then insert this info using sql queries into a new entry for this specific order.
            elif ord_option == '2':
                cust_name = input('Please enter customer name: ')
                cust_address = input('Please enter customers full address: ')
                cust_phone = input('Please enter customer phone number: ')
                
                show_prod_list(cursor)
                prod_input = int(input('Please select the number of the product the customer has ordered: '))
                print()
                
                show_courier_list(cursor)
                cour_input = int(input('Please select the number of the courier you wish to use: '))
                
                sql = 'INSERT INTO orders (customer_name, customer_address, customer_phone, product_id, courier_id, order_status_id) VALUES (%s, %s, %s, %s, %s, 1)' 
                val = (cust_name, cust_address, cust_phone, prod_input, cour_input)
                cursor.execute(sql,val)
                connection.commit()
                print()
                print(cursor.rowcount, "Order inserted successfully into orders table")
                print()
                show_order_list(cursor)
                
            # 3 to update order status
            elif ord_option == '3':
                show_order_status(cursor)
                print()
                print('-The above table shows the order ID with its corresponding status-')
                print()
            
                upd_ord = int(input('Please select the order number of the status you want to update: '))
                print()
                show_order_status_list(cursor)
                new_status = int(input('Please select the new status for this order: '))
                
                sql = 'UPDATE orders SET order_status_id=%s WHERE order_id=%s'
                val = (new_status,upd_ord)
                cursor.execute(sql,val)
                connection.commit()
                print()
                print(f"Order {upd_ord} status updated successfully")
                print()
                show_order_status(cursor)
                
            # 4 will update an existing order. much like creating new order but is updating an existing index
            elif ord_option == '4':
                show_order_list(cursor)
                
                upd_order = int(input('Please select the number of the order you wish to update: '))
                cust_name = input('Please enter updated customer name: ')
                cust_address = input('Please enter customers updated address: ')
                cust_phone = input('Please enter customers updated phone number: ')
                
                show_prod_list(cursor)
                prod_input = int(input('Please select the number of the product the customer has ordered: '))
                
                show_courier_list(cursor)
                cour_input = int(input('Please select the number of the courier you wish to use: '))
                
                sql = 'UPDATE orders SET customer_name=%s, customer_address=%s, customer_phone=%s, product_id=%s, courier_id=%s, order_status_id=1 WHERE order_id=%s'
                val = (cust_name,cust_address,cust_phone,prod_input,cour_input,upd_order)
                cursor.execute(sql,val)
                connection.commit()
                print()
                print(cursor.rowcount, "Order updated successfully")
                print()
                show_order_list(cursor)
        
            
            
            # to delete order. uses same logic as product and courier db deletions
            elif ord_option == '5':
                show_order_list(cursor)
                delete_order(cursor,connection)
                show_order_list(cursor)
            
            else:
                print('Error')
                print('Please select a valid order menu option')

                    
    # entering any option not listed will print the below message and loop back to main menu        
    else:
        print('Error')
        print('Please select a valid main menu option')