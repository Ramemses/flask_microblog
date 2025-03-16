from flask import render_template, redirect, url_for, flash, request
from my_app import app
from my_app.forms import LoginForm



@app.route('/')
@app.route('/index')
def index():
	user = {"username": "Jhon"}
	posts = [
		{
			"author": {"username": "Mike"},
			"body": "The weather is great!"
		},
		{
			"author": {"username": "Kenni"},
			"body": "I will kill you"
		},
	]


	return render_template('index.html', title="Главная", user=user, posts=posts)


@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	
	if request.method == 'POST':
		print(request.form)
	
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))		
		redirect( url_for('index') )


	return render_template('login.html', title='Sign in', form = form)

	
