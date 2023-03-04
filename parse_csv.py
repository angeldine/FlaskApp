import csv

import sqlite3

# open the connection to the database
conn = sqlite3.connect('us_superstore_data.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS orders')
conn.execute('DROP TABLE IF EXISTS customers')
conn.execute('DROP TABLE IF EXISTS products')
conn.execute('DROP TABLE IF EXISTS links')

print("tables dropped successfully")

# create table again
conn.execute('CREATE TABLE products (Id INTEGER PRIMARY KEY AUTOINCREMENT, Product_Id TEXT, Product_Name TEXT, Category TEXT, Subcategory TEXT, Price REAL, Quantity INTEGER)')
conn.execute('CREATE TABLE customers (Id INTEGER PRIMARY KEY AUTOINCREMENT, Customer_Id TEXT, Customer_Name TEXT, Segment TEXT, city TEXT, state TEXT, postal TEXT, Country TEXT)')
conn.execute('CREATE TABLE orders (Id INTEGER PRIMARY KEY AUTOINCREMENT,  Order_Id TEXT, customer_id INTEGER, Order_Date TEXT, Ship_Date TEXT, Ship_Mode TEXT, FOREIGN KEY(customer_id) REFERENCES customers(Id))')
conn.execute('CREATE TABLE links (id INTEGER PRIMARY KEY AUTOINCREMENT, customer_id TEXT, customer_name TEXT, order_id TEXT, order_date TEXT, product_id TEXT, product_name TEXT, cost REAL, quantity INTEGER, FOREIGN KEY(customer_id) REFERENCES customers(Customer_Id), FOREIGN KEY(order_id) REFERENCES orders(Order_Id), FOREIGN KEY(product_id) REFERENCES products(Product_Id))')
print("tables created successfully")




with open('us_superstore.csv', newline='') as f:
   reader = csv.reader(f, delimiter=",")
   next(reader) # skip the header line
 
   for p in reader:
      # print(p)
      Product_Id = p[13]
      Product_Name = p[16]
      Category = p[14]
      Subcategory = p[15]
      Price = float(p[17])
      Quantity = int(p[18])

      cur.execute('INSERT INTO products VALUES (NULL,?,?,?,?,?,?)', (Product_Id, Product_Name, Category, Subcategory, Price, Quantity))
      conn.commit()
   print("data parsed successfully")




with open('us_superstore.csv', newline='') as f:
   reader = csv.reader(f, delimiter=",")
   next(reader) # skip the header line

# for customers table
   for c in reader:
      # print(c)

      Customer_Id = c[5]
      Customer_Name = c[6]
      Segment = c[7]
      city = c[9]
      state = c[10]
      postal = c[11]
      Country = c[8]
      cur.execute('INSERT INTO customers VALUES (NULL,?,?,?,?,?,?,?)', (Customer_Id, Customer_Name, Segment, city, state, postal, Country))
      conn.commit()

with open('us_superstore.csv', newline='') as f:
   reader = csv.reader(f, delimiter=",")
   next(reader) # skip the header line
   

   # cur.execute('select * from customers')
   # customers = cur.fetchall()
   for row in reader:
      Order_Id = row[1]
      Order_Date = row[2]
      Ship_Date = row[3]
      Ship_Mode = row[4]
      customer_id = row[5]
      cur.execute('INSERT INTO orders VALUES (NULL,?,?,?,?,?)', (Order_Id, customer_id, Order_Date, Ship_Date, Ship_Mode))
      conn.commit()
   print("data parsed successfully")


with open('us_superstore.csv', newline='') as f:
   reader = csv.reader(f, delimiter=",")
   next(reader) # skip the header line

   for link in reader:
      order_id = link[1]
      order_date = link[2]
      customer_id = link[5]
      customer_name = link[6]
      product_id = link[13]
      product_name = link[16]
      cost = float(link[17])
      quantity = int(link[18])
      cur.execute('INSERT INTO links VALUES (NULL,?,?,?,?,?,?,?,?)', (customer_id, customer_name, order_id, order_date, product_id, product_name, cost, quantity))
      conn.commit()
   print("data parsed successfully")


         

         
      

   

conn.close()   
