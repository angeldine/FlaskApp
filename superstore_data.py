import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # open the connection to the database
    conn = sqlite3.connect('us_superstore_data.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * FROM orders limit 20")
    rows = cur.fetchall()
    conn.close()
    return render_template('index.html', rows=rows)


@app.route('/customers')
def customers():
    # open the connection to the database
    conn = sqlite3.connect('us_superstore_data.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * FROM customers limit 20")
    customer = cur.fetchall()
    conn.close()
    return render_template('customers.html', customer=customer)


@app.route('/products')
def products():
    # open the connection to the database
    conn = sqlite3.connect('us_superstore_data.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * FROM products limit 20")
    product = cur.fetchall()
    conn.close()
    return render_template('products.html', product=product)