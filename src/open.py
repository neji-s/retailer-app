def open_app(db_cursor, db_connection):
    sql = '''CREATE TABLE IF NOT EXISTS products(
                product_id INT NOT NULL AUTO_INCREMENT,
                product_name VARCHAR(255) NOT NULL,
                product_price VARCHAR(255) NOT NULL,
                PRIMARY KEY (product_id)
            );

            CREATE TABLE IF NOT EXISTS couriers(
                courier_id INT NOT NULL AUTO_INCREMENT,
                courier_name VARCHAR(255) NOT NULL,
                courier_phone VARCHAR(255) NOT NULL,
                PRIMARY KEY (courier_id)
            );

            CREATE TABLE IF NOT EXISTS order_status(
                order_status_id INT NOT NULL AUTO_INCREMENT,
                order_status VARCHAR(255) NOT NULL,
                PRIMARY KEY (order_status_id)
            );

            CREATE TABLE IF NOT EXISTS orders(
                order_id INT NOT NULL AUTO_INCREMENT,
                customer_name VARCHAR(255) NOT NULL,
                customer_address VARCHAR(255) NOT NULL,
                customer_phone VARCHAR(255) NOT NULL,
                product_id INT NOT NULL,
                courier_id INT NOT NULL,
                order_status_id INT NOT NULL,
                PRIMARY KEY (order_id),
                FOREIGN KEY (product_id) REFERENCES products(product_id),
                FOREIGN KEY (courier_id) REFERENCES couriers(courier_id),
                FOREIGN KEY (order_status_id) REFERENCES order_status(order_status_id)
            );

            INSERT INTO products (product_name, product_price) 
            VALUES ('jumper', '10.5');

            INSERT INTO couriers (courier_name, courier_phone) 
            VALUES ('steve', '079');

            INSERT INTO order_status (order_status)
            VALUES ('accepted', 'packing', 'out for delivery', 'delivered');

            INSERT INTO orders (customer_name, customer_address, customer_phone, product_id, courier_id, order_status_id) 
            VALUES ('harry potter', '4 privet drive', '078', 1, 1, 1);'''
            
    db_cursor.execute(sql, multi=True)
    db_connection.commit()