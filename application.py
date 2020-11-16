from flask import Flask, render_template, make_response, request, jsonify, url_for, redirect, json
from flask_sqlalchemy import SQLAlchemy
import base64
import os

application = Flask(__name__)
if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'PostgreSQL',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
# application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/portf_test_db'
# application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)


# class Project(db.Model):
#     __tablename__ = 'project'
#     id = db.Column(db.Integer, primary_key=True)
#     thumbnail = db.Column(db.LargeBinary, nullable=False)
#     title = db.Column(db.String, nullable=False)
#     description = db.Column(db.String, nullable=False)
#     github_link = db.Column(db.String, nullable=True)
#     link = db.Column(db.String, nullable=True)
#     time_created = db.Column(db.Integer, nullable=False)
#
#     def __repr__(self):
#         return f'id : {self.id}, desc: {self.title}, descrip : {self.description}, image : {self.thumbnail}'
#


class Portfolio_test():
    __tablename__ = 'Portfolio_test'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'id :{self.id}, fname: {self.fullname}, username: {self.username}, email: {self.email}'


db.create_all()

if 'RDS_HOSTNAME' in os.environ:
    print(os.environ)


# print(os.environ)
@application.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@application.route('/about')
def about():
    return render_template('about.html')


@application.route('/test')
def test():
    body_data = []
    all_data1 = Portfolio_test.query.all()
    # image_data = Project.query.filter_by(id=5).first()
    # image = base64.b64encode(image_data.thumbnail).decode('ascii')
    # print(image_data1)
    for i in all_data1:
        the_data = {
            'id': i.id,
            'fullname': i.fullname,
            'username': i.username,
            'email': i.email,
            # 'img': base64.b64encode(i.thumbnail).decode('ascii')
        }
        body_data.append(the_data)
    print(body_data)
    return render_template('test.html', data=body_data)


# @application.route('/works/<pid>')
# def work_link(pid):
#     try:
#         get_project = Project.query.filter_by(title=pid).first()
#         data_d = {
#             'id': get_project.id,
#             'title': get_project.title,
#             'desc': get_project.description,
#             'img': base64.b64encode(get_project.thumbnail).decode('ascii')
#         }
#         return render_template('work.html', data=data_d)
#     except:
#         return render_template('404.html')


# @application.route('/works')
# def works():
#     body_data = []
#     all_data1 = Project.query.all()
#     # image_data = Project.query.filter_by(id=5).first()
#     # image = base64.b64encode(image_data.thumbnail).decode('ascii')
#     # print(image_data1)
#     for i in all_data1:
#         the_data = {
#             'id': i.id,
#             'handle': i.title,
#             'desc': i.description,
#             'img': base64.b64encode(i.thumbnail).decode('ascii')
#         }
#         body_data.append(the_data)
#     print(body_data)
#     return render_template('works.html', data=body_data)


# @application.route('/works')
# def works():
#     return render_template('works.html')


@application.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')


@application.route('/components')
def components():
    return render_template('components.html')


@application.errorhandler(404)
def not_found(e):
    """Page not found."""
    return make_response(render_template("404.html"), 404)


@application.errorhandler(400)
def bad_request(e):
    """Bad request."""
    return make_response(render_template("400.html"), 400)


@application.errorhandler(500)
def server_error(e):
    """Internal server error."""
    return make_response(render_template("500.html"), 500)


if __name__ == '__main__':
    application.run(debug=True)
