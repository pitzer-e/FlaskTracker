from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    first_name = db.Column(db.String(length=30), nullable=False, unique=True)
    last_name = db.Column(db.String(length=30), nullable=False, unique=True)
    user_name = db.Column(db.String(length=30), nullable=False, unique=True)
    is_infected = db.Column(db.Boolean(), nullable=False, default=False)
    user_id = db.Column(db.Integer(), primary_key=True)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/data')
def data_page():
    return render_template('data.html')


@app.route('/report')
def report_page():
    return render_template('report.html', item_name="Place")


@app.route('/admin')
def admin_page():
    users = User.query.all()
    return render_template('admin.html', users=users)
