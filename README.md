# FlaskApp
# Database-Driven web application developed in Python with Flask and Sqlite3
This dynamic web application is designed for a furniture retail superstore known as
 DiamondzFurniture based in the US.

The web app displays the dataset of the company from 2014-2018. 
This contains records from the customer, orders made by customers and the different product purchased within
the period.

Data of over 2000 records have been collated within the four year period, but a total of 30 records is displayed
for efficiency and readability.

The web application in developed using Flask framework and Sqlite3 database and has been deployed on github: git@github.com:angeldine/FlaskApp.git
and Render: https://flask-app-zae9.onrender.com. You can access the application by performing the following:


## Set up the Repository
Pull this Git repository into your system so that you have everything to get started.

        git clone git@github.com:angeldine/FlaskApp.git

We need to start by setting up our development environment by executing these commands in the terminal, that's open in the diretory were we've cloned this repo.

        pyenv local 3.7.0 # this sets the local version of python to 3.7.0
        python3 -m venv .venv # this creates the virtual environment for you
        source .venv/bin/activate # this activates the virtual environment
        pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.


        pip install flask
        pip install behave
        pip install selenium

## Setting up the Application


Load the application settings into your terminal and start the server with 

        export FLASK_APP=superstore_data.py 
        export FLASK_ENV=development
        python3 -m flask run --host 0.0.0.0

## Check the tests

You can run the current tests to see that the customer pages load, with the command

        behave

in the terminal. 

##  Going through the Web App
The first page - index.html is the home page with a brief description of the store. There are links to customers page,
orders and products page.
You can click on a customer ID to view the purchase made by that customer within the period,similarly, the orders and products
page also displays information for each product and order made by any customer.
