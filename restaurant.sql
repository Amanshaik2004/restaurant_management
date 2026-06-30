Create database restaurant_db;

use restaurant_db;

CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO roles (role_name)
VALUES
('Admin'),
('Manager'),
('Waiter'),
('Chef'),
('Customer');

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,

    username VARCHAR(100) NOT NULL,

    email VARCHAR(100) UNIQUE NOT NULL,

    password_hash VARCHAR(255) NOT NULL,

    role_id INT NOT NULL,

    FOREIGN KEY(role_id)
    REFERENCES roles(id)
);

INSERT INTO users
(username,email,password_hash,role_id)
VALUES
(
'admin',
'admin@gmail.com',
'admin123',
1
),
(
'manager',
'manager@gmail.com',
'manager123',
2
),
(
'waiter',
'waiter@gmail.com',
'waiter123',
3
),
(
'chef',
'chef@gmail.com',
'chef123',
4
),
(
'customer',
'customer@gmail.com',
'customer123',
5
);

CREATE TABLE restaurants (

    id INT AUTO_INCREMENT PRIMARY KEY,

    restaurant_name VARCHAR(100) NOT NULL,

    owner_name VARCHAR(100) NOT NULL,

    email VARCHAR(100) UNIQUE NOT NULL,

    phone VARCHAR(15) UNIQUE NOT NULL,

    address VARCHAR(255) NOT NULL,

    opening_time TIME NOT NULL,

    closing_time TIME NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO restaurants
(
restaurant_name,
owner_name,
email,
phone,
address,
opening_time,
closing_time
)
VALUES
(
'Food Palace',
'Rahul',
'foodpalace@gmail.com',
'9876543210',
'Hyderabad',
'09:00:00',
'23:00:00'
);

CREATE TABLE restaurant_tables (

    id INT AUTO_INCREMENT PRIMARY KEY,

    table_number INT UNIQUE NOT NULL,

    capacity INT NOT NULL,

    status ENUM(
        'Available',
        'Reserved',
        'Occupied'
    ) DEFAULT 'Available',

    restaurant_id INT NOT NULL,

    FOREIGN KEY (restaurant_id)
    REFERENCES restaurants(id)
);

INSERT INTO restaurant_tables
(table_number,capacity,restaurant_id)
VALUES
(1,2,1),
(2,4,1),
(3,6,1),
(4,8,1);

CREATE TABLE categories (

    id INT AUTO_INCREMENT PRIMARY KEY,

    category_name VARCHAR(100) UNIQUE NOT NULL,

    description VARCHAR(255)
);

INSERT INTO categories
(category_name, description)
VALUES
('Starters','Starter dishes'),
('Main Course','Main meals'),
('Desserts','Sweet dishes'),
('Drinks','Beverages');

CREATE TABLE menu_items (

    id INT AUTO_INCREMENT PRIMARY KEY,

    item_name VARCHAR(100) NOT NULL,

    description VARCHAR(255),

    price DECIMAL(10,2) NOT NULL,

    image_url VARCHAR(255),

    is_available BOOLEAN DEFAULT TRUE,

    category_id INT NOT NULL,

    FOREIGN KEY(category_id)
    REFERENCES categories(id)
);

INSERT INTO menu_items
(
item_name,
description,
price,
category_id
)
VALUES
(
'Chicken Biryani',
'Hyderabadi Dum Biryani',
250,
2
),
(
'Veg Fried Rice',
'Chinese Rice',
180,
2
),
(
'Chocolate Cake',
'Fresh Chocolate Cake',
120,
3
),
(
'Coca Cola',
'Cold Drink',
50,
4
),
(
'Chicken 65',
'Spicy Chicken Starter',
220,
1
);

CREATE TABLE orders (

    id INT AUTO_INCREMENT PRIMARY KEY,

    customer_name VARCHAR(100) NOT NULL,

    restaurant_id INT NOT NULL,

    table_id INT NOT NULL,

    order_status ENUM(
        'Pending',
        'Preparing',
        'Ready',
        'Completed',
        'Cancelled'
    ) DEFAULT 'Pending',

    order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (restaurant_id)
    REFERENCES restaurants(id),

    FOREIGN KEY (table_id)
    REFERENCES restaurant_tables(id)
);

INSERT INTO orders
(
customer_name,
restaurant_id,
table_id
)
VALUES
(
'Aman',
1,
2
);

CREATE TABLE order_items (

    id INT AUTO_INCREMENT PRIMARY KEY,

    order_id INT NOT NULL,

    menu_item_id INT NOT NULL,

    quantity INT NOT NULL,

    price DECIMAL(10,2) NOT NULL,

    FOREIGN KEY(order_id)
    REFERENCES orders(id),

    FOREIGN KEY(menu_item_id)
    REFERENCES menu_items(id)
);

INSERT INTO order_items
(
order_id,
menu_item_id,
quantity,
price
)
VALUES
(1,1,2,250),
(1,4,2,50),
(1,3,1,120);

CREATE TABLE bills (

    id INT AUTO_INCREMENT PRIMARY KEY,

    order_id INT NOT NULL,

    subtotal DECIMAL(10,2) NOT NULL,

    tax DECIMAL(10,2) DEFAULT 0,

    discount DECIMAL(10,2) DEFAULT 0,

    total_amount DECIMAL(10,2) NOT NULL,

    payment_status ENUM(
        'Pending',
        'Paid'
    ) DEFAULT 'Pending',

    FOREIGN KEY(order_id)
    REFERENCES orders(id)
);

INSERT INTO bills
(
order_id,
subtotal,
tax,
discount,
total_amount,
payment_status
)
VALUES
(
1,
720,
36,
20,
736,
'Paid'
);

CREATE TABLE inventory (

    id INT AUTO_INCREMENT PRIMARY KEY,

    ingredient_name VARCHAR(100) NOT NULL,

    quantity DECIMAL(10,2) NOT NULL,

    unit VARCHAR(20) NOT NULL,

    minimum_stock DECIMAL(10,2) NOT NULL
);

INSERT INTO inventory
(
ingredient_name,
quantity,
unit,
minimum_stock
)
VALUES
('Rice',50,'Kg',10),
('Chicken',25,'Kg',5),
('Cooking Oil',30,'Litres',5),
('Onion',40,'Kg',8),
('Tomato',35,'Kg',8);

CREATE TABLE notifications (

    id INT AUTO_INCREMENT PRIMARY KEY,

    message VARCHAR(255),

    status ENUM(
        'Sent',
        'Pending'
    ) DEFAULT 'Pending',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO notifications(message)
VALUES
('Order Confirmed'),
('Order Ready'),
('Table Reserved');

CREATE TABLE audit_logs (

    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT,

    activity VARCHAR(255),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
    REFERENCES users(id)
);

INSERT INTO audit_logs
(user_id,activity)
VALUES
(1,'User Logged In'),
(2,'Menu Updated'),
(3,'Order Completed');
