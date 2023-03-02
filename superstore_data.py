import sqlite3
from flask import Flask, g, render_template

app = Flask(__name__)

app.config.from_object(__name__)

# database details - to remove some duplication
db_name = 'us_superstore_data.db'

# code based on example at https://github.com/mjhea0/flaskr-tdd

def connect_db():
    conn = sqlite3.connect(db_name, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn.row_factory = sqlite3.Row
    return conn

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()



@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/orders')
def orders():
    # open the connection to the database
    db = get_db()
    cur = db.execute("select * FROM orders limit 30")
    rows = cur.fetchall()
    return render_template('orders.html', rows=rows)


@app.route('/customers')
def customers():
    # open the connection to the database
    db = get_db()
    cur = db.execute("select * FROM customers limit 30")
    customer = cur.fetchall()
    return render_template('customers.html', customer=customer)


@app.route('/products')
def products():
    # open the connection to the database
    db = get_db()
    cur = db.execute("select * FROM products limit 30")
    product = cur.fetchall()
    return render_template('products.html', product=product)


@app.route('/customer_details/<id>')
def customer_details(id):
    db = get_db()
    # cur.execute("SELECT customers.Customer_Id, orders.Order_Id, customers.Customer_Name FROM orders, customers WHERE orders.customer_id = customers.Customer_Id AND customers.Customer_Id = ?", (id,))
    cur = db.execute("SELECT * from links WHERE customer_id = ?", (id,))
    cus = cur.fetchall()
    return render_template('customer_details.html', customer=cus)


@app.route('/order_details/<id>')
def order_details(id):
    db = get_db()
    # cur.execute("SELECT customers.Customer_Id, orders.Order_Id, customers.Customer_Name FROM orders, customers WHERE orders.customer_id = customers.Customer_Id AND customers.Customer_Id = ?", (id,))
    cur = db.execute("SELECT * from links WHERE order_id = ?", (id,))
    cus = cur.fetchall()
    return render_template('order_details.html', order=cus)

