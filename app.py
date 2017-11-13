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

		return redirect(url_for('home'))
	return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':

		username = request.form['username']
		password_actual = request.form['password']
		if username:
			print(username)
			print(password_actual)
		cursor = mariadb_connection.cursor(buffered=True,dictionary=True)
		cursor.execute("SELECT * FROM users WHERE username = %s", [username])
		data = cursor.fetchone()
		if data:
			print data["password"]
		password = data["password"]
		if sha256_crypt.verify(password_actual, password):
			session['loggedin'] = True
			session['username'] = username
 			flash('password matched')
			return redirect(url_for('topics'))
		else:
			flash('password not matched')
			return render_template('login.html')
		cursor.close()

	return render_template('login.html')	

@app.route('/logout')
def logout():
	session.clear()
	flash("loggewd ouuut")
	return redirect(url_for('login'))

@app.route('/topics')
def topics():
	return render_template('topics.html')

if __name__ == "__main__":
	app.secret_key='secret123'
	app.run()



