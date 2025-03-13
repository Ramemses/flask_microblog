from flask import render_template
from my_app import app



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
