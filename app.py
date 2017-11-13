from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from data import Articles
import mysql.connector as mariadb
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

#db config
mariadb_connection = mariadb.connect(user='root', database='python1')


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
		name = form.name.data
		username = form.username.data
		email = form.email.data
		password = sha256_crypt.encrypt(str(form.password.data))

		#cursor
		cursor = mariadb_connection.cursor()
		cursor.execute("INSERT INTO users(name, email, username, password) VALUES (%s, %s, %s, %s)", (name, email, username, password))

		mariadb_connection.commit()

		cursor.close()

		flash("youy are now registered and can login")

		redirect(url_for('home'))
	return render_template('register.html', form=form)

if __name__ == "__main__":
	app.secret_key='secret123'
	app.run()