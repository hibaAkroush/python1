from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
# from data import Articles
import mysql.connector as mariadb
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
import urllib2
import re

app = Flask(__name__)

#db config
mariadb_connection = mariadb.connect(user='root', database='python1')


# Articles = Articles()

@app.route("/", methods=['GET', 'POST'])
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

# @app.route('/login', methods=['GET', 'POST'])


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'loggedin' in session:
            return f(*args, **kwargs)
        else:
            flash('Please login')
            return redirect(url_for('login'))
    return wrap

@app.route('/logout')
def logout():
	session.clear()
	flash("loggewd ouuut")
	return redirect(url_for('login'))

@app.route('/topics')
@is_logged_in
def topics():
	return render_template('topics.html')

class topicForm(Form):
    title = StringField(u'title', validators=[validators.Length(min=1, max=250)])
    img  = StringField(u'img', validators=[validators.Length(min=6, max=300)])
    content = StringField('content', validators=[validators.Length(min=6)] )
    url = StringField('url', validators=[validators.Length(min=6, max=300)] )

@app.route('/fetch')
@is_logged_in
def fetch():
	form = topicForm(request.form)
	urls = []

	mainurl = "http://www.mathhelp.com/intermediate-algebra-help/?utm_campaign=purplemath&utm_source=_mh_cima&utm_medium=course"
	req = urllib2.Request(mainurl)
	response = urllib2.urlopen(req)
	the_page = response.read()
	# took first 5 urls to make fetching fatser for testing
	allurls = re.findall(r'/how_to/(.*?)">', str(the_page))
	urls  = allurls[0:5]
	j=0
	while j<5:
		temp = urls[j]
		urls[j] = "http://www.mathhelp.com/how_to/"+urls[j]
		j+=1

	listOfTopics = []
	i=0
	while i<len(urls):
		x = {}
		req = urllib2.Request(urls[i])
		response = urllib2.urlopen(req)
		the_page = response.read()
		title = re.findall(r'<title>(.*?)</title>', str(the_page))
		img = re.findall(r'<img src="(.*?)"', str(the_page))
		content = re.findall(r'</h1><p>(.*?)</p>', str(the_page))
		url = urls[i]
		x.update({"img":img[1]})
		x.update({"title":title})
		x.update({"url":url})
		x.update({"id":i})
		x.update({"content":content})
		listOfTopics.append(x)
		i+=1
	print listOfTopics
	# def Articles():
	# 	articles = listOfTopics
	# 	return articles
# , articles = listOfTopics
	return render_template('topics.html', articles = listOfTopics)

if __name__ == "__main__":
	app.secret_key='secret123'
	app.run()



