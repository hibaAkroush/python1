from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

Articles = Articles()

@app.route("/")
def home():
    return render_template('home.html',articles = Articles)

class registerForm(Form):
    name = StringField(u'First Name', validators=[validators.Length(min=1, max=50)])
    username  = StringField(u'User Name', validators=[validators.Length(min=4, max=25)])
    email = StringField('email', validators=[validators.Length(min=6, max=50)] )
    password = StringField('password', validators=[validators.DataRequired(),
    	validators.EqualTo('confirm', message='password does not match')
    	] )
    confirm = PasswordField('confirm password')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form  = registerForm(request.form)
	if request.method == 'POST' and form.validate():
		return render_template('register.html')
	return render_template('register.html', form=form)

if __name__ == "__main__":
    app.run()