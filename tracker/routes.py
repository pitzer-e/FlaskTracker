from tracker import app
from flask import render_template
from tracker.models import User


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
