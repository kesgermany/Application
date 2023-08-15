from application import app, db
from application.models import Products
from application.models import Customer
from flask import Flask, render_template, request
from flask import jsonify


@app.route('/customers', methods=['GET'])
def customers():
    customers = Customer.query.all()
    return jsonify([customer.to_json() for customer in customers])




















