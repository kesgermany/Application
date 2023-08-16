from typing import Any
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length

class ContactForm(FlaskForm):
    first_name = StringField('First Name', validators=[
        DataRequired(),
        Length(min=2, max=30)
    ])
    last_name = StringField('Last Name')
    message = StringField('Type your message', validators=[
        DataRequired(),
        DataRequired(),
        Length(min=10, max=100)
    ])
    submit = SubmitField('Send')