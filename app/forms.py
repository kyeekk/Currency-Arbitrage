from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextAreaField, TextField, SelectField
from wtforms.validators import DataRequired, Email


class Form(FlaskForm):
    amount = TextField('Amount: ')
    currencies = SelectField("From: ", choices = [('USD', 'United States Dollar'),('EUR', 'Euro'),('GBP', 'British Pound'),
                        ('AUD', 'Australian Dollar'),('NZD', 'NZD'),('JMD', 'Jamaican Dollar'),('ZAR', 'ZAR'),('CAD', 'Canadian Dollar'),
                        ('CHF', 'Swiss Franc'),('JPY', 'Japanese Yen')])
    currencies1 = SelectField("To: ", choices = [('USD', 'United States Dollar'),('EUR', 'Euro'),('GBP', 'British Pound'),
                        ('AUD', 'Australian Dollar'),('NZD', 'NZD'),('JMD', 'Jamaican Dollar'),('ZAR', 'ZAR'),('CAD', 'Canadian Dollar'),
                        ('CHF', 'Swiss Franc'),('JPY', 'Japanese Yen')])