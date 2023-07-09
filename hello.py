from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Create a Flask Instance
app = Flask(__name__) # way to always start.  finds files
app.config['SECRET_KEY'] = "my super secret key"

# Create a form class
class NamerForm(FlaskForm):
	name = StringField("What's Your Name?", validators =[DataRequired()])
	submit = SubmitField("Submit")

# BooleanField
# DateField
# DateTimeField
# DecimalField
# FileField
# HiddenField
# MultipleField
# FieldList
# FloatField
# FormField
# IntegerField
# PasswordField
# RadioField
# SelectField
# SelectMultipleField
# SubmitField
# StringField
# TextAreaField

## Validators
# DataRequired
# Email
# EqualTo
# InputRequired
# IPAddress
# Length
# MacAddress
# NumberRange
# Optional
# Regexp
# URL
# UUID
# AnyOf
# NoneOf


# Create a route decorator
@app.route('/') # main webpage

#def index():
#	return "<h1>Hello World!</h1>"

# Filters

#safe makes html safe
#capitalize
#lower 
#upper 
#title capitalize first letter in each word
#trim removes trailing space from the end
#striptags strips html tags


def index():
	my_name = "Chris"
	stuff = "This is <strong>Bold</strong> Text"

	favorite_pizza = ["Pepperoni", "Cheese", "Sausage", "All Meat", 41]
	return render_template("index.html", first_name=my_name,
		my_stuff=stuff, favorite_pizza = favorite_pizza)

# localhost:5000/user/Chris
@app.route('/user/<name>' )

#def user(name):
	#return "<h1>Hello {}!!</h1>".format(name)

def user(name):
	return render_template("user.html", user_name=name)

# Create Custom Error Pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500

#Create Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
	name = None
	form = NamerForm()

	#Validate Form
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
		flash("Form Submitted Successfully!")


	return render_template("name.html", name = name,
		form = form)




