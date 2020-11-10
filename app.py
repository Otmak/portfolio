from flask import Flask, render_template, request, jsonify, url_for, redirect, json
from flask_sqlalchemy import SQLAlchemy
import base64

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/portfolio_db_test_1'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# class Project(db.Model):
#     __tablename__ = 'project'
#     id = db.Column(db.Integer, primary_key=True)
#     thumbnail = db.Column(db.LargeBinary, nullable=False)
#     title = db.Column(db.String, nullable=False)
#     description = db.Column(db.String, nullable=False)
#     github_link = db.Column(db.String, nullable=True)
#     link = db.Column(db.String, nullable=True)

#     def __repr__(self):
#         return f'id : {self.id}, desc: {self.title}, descrip : {self.description}, image : {self.thumbnail}'

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/portf_test_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
#
# class Project(db.Model):
#     __tablename__ = 'project'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String, nullable=False)
#     description = db.Column(db.String, nullable=False)
#     thumbnail = db.Column(db.LargeBinary, nullable=False)
#
#     def __repr__(self):
#         return f'id : {self.id}, desc: {self.title}, descrip : {self.description}, image : {self.thumbnail}'
#
#
# db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/work')
def work():
    return render_template('work.html')


# @app.route('/works/<pid>')
# def work_link(pid):
#     get_project = Project.query.filter_by(title=pid).first()
#     data_d = {
#         'id':get_project.id,
#         'title': get_project.title,
#         'desc': get_project.description,
#         'img': base64.b64encode(get_project.thumbnail).decode('ascii')
#     }
#     return render_template('work.html', data=data_d)
#

# @app.route('/works')
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
#         # data = json.dumps(data_dump)
#     return render_template('works.html', data=body_data)


@app.route('/works')
def works():
    return render_template('works.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')


@app.route('/components')
def components():
    return render_template('components.html')


if __name__ == '__main__':
    app.run()
