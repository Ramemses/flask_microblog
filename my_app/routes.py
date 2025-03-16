from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required 
import sqlalchemy as sa
from urllib.parse import urlsplit

from my_app import app, db
from my_app.forms import LoginForm, RegistrationForm
from my_app.models import User



@app.route('/')
@app.route('/index')
@login_required
def index():
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


	return render_template('index.html', title="Главная", posts=posts)


@app.route('/login', methods = ['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect( url_for('index') )
	form = LoginForm()
	if form.validate_on_submit():
		user = db.session.scalar(sa.select(User).where(User.username == form.username.data))
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('login'))
	
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or urlsplit(next_page).netloc != '':
			next_page = url_for('index')
		return redirect(next_page)
	return render_template('login.html', title='Sign in', form=form)
	

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))

	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()

		flash('Congratulations, you are registered user for now!')	
		return redirect(url_for('login'))
	return render_template('register.html', title = 'Register', form=form)
