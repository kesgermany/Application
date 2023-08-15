from application import app, db
from application.models import Products
from application.models import Customer
from flask import Flask, render_template, request
from flask import jsonify
from form import ContactForm


@app.route('/customers', methods=['GET'])
def customers():
    customers = Customer.query.all()
    return jsonify([customer.to_json() for customer in customers])

@app.route('/')
def home():
    return render_template('frontend.html')

@app.route('/contactform')
def contactform():
    form = ContactForm()
    return render_template('contactform.html', form=form)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')


@app.route('/payment')
def payment():
    return render_template('payment.html')


@app.route('/productlisting')
def product_listing():
    return render_template('productlisting.html')


@app.route('/cart')
def cart():
    return render_template('cart.html')


@app.route('/about')
def about():
    return render_template('about.html')





















