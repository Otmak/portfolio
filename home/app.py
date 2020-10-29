
from flask import Flask, render_template, request, jsonify,url_for,redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/example2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route( '/about')
def about():
	return render_template('about.html')


@app.route( '/work')
def work():
	return render_template('work.html')


@app.route( '/works')
def works():
	return render_template('works.html')


@app.route( '/contact', methods=['GET', 'POST'])
def contact():
	return render_template('contact.html')


@app.route( '/components')
def components():
	return render_template('components.html')
