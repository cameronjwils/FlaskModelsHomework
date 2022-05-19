from app import app
from flask import render_template
from models import orders_placed
from models.orders_placed import orders

@app.route('/')
def index():
    return render_template('index.html', title='TheHoodieShop', orders=orders)

