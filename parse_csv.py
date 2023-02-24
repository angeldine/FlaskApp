import csv

import sqlite3

# open the connection to the database
conn = sqlite3.connect('us_superstore_data.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS orders')
conn.execute('DROP TABLE IF EXISTS customers')
conn.execute('DROP TABLE IF EXISTS products')
print("tables dropped successfully")

# create table again
conn.execute('CREATE TABLE products (Id INTEGER PRIMARY KEY AUTOINCREMENT, Product_Id TEXT, Product_Name TEXT, Price REAL, Quantity INTEGER)')
conn.execute('CREATE TABLE customers (Id INTEGER PRIMARY KEY AUTOINCREMENT, Customer_Id TEXT, Customer_Name TEXT, Segment TEXT, Country TEXT)')
conn.execute('CREATE TABLE orders (Id INTEGER PRIMARY KEY AUTOINCREMENT,  Order_Id TEXT, customer_id INTEGER, Order_Date TEXT, Ship_Date TEXT, Ship_Mode TEXT, FOREIGN KEY(customer_id) REFERENCES customers(Id))')
print("tables created successfully")




with open('data.csv', newline='') as f:
   reader = csv.reader(f, delimiter=",")
   next(reader) # skip the header line
 
   for p in reader:
      # print(p)
      Product_Id = p[13]
      Product_Name = p[16]
      Price = float(p[17])
      Quantity = int(p[18])

      cur.execute('INSERT INTO products VALUES (NULL,?,?,?,?)', (Product_Id, Product_Name, Price, Quantity))
      conn.commit()
   print("data parsed successfully")




with open('data.csv', newline='') as f:
   reader = csv.reader(f, delimiter=",")
   next(reader) # skip the header line

# for customers table
   for c in reader:
      # print(c)

      Customer_Id = c[5]
      Customer_Name = c[6]
      Segment = c[7]
      Country = c[8]
      cur.execute('INSERT INTO customers VALUES (NULL,?,?,?,?)', (Customer_Id, Customer_Name, Segment, Country))
      conn.commit()

with open('data.csv', newline='') as f:
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
  
   
         

         
   

   

conn.close()   
