from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextAreaField, TextField, SelectField
from wtforms.validators import DataRequired, Email


class Form(FlaskForm):
    currencies = SelectField("Currency 1", choices = [('USD', 'USD'),('EUR', 'EUR'),('GBP', 'GBP'),('AUD', 'AUD'),('NZD', 'NZD'),('JMD', 'JMD'),('ZAR', 'ZAR'),('CAD', 'CAD'),('CHF', 'CHF'),('JPY', 'JPY')])
    currencies1 = SelectField("Currency 2",  choices = [('USD', 'USD'),('EUR', 'EUR'),('GBP', 'GBP'),('AUD', 'AUD'),('NZD', 'NZD'),('JMD', 'JMD'),('ZAR', 'ZAR'),('CAD', 'CAD'),('CHF', 'CHF'),('JPY', 'JPY')])
