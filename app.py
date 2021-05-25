from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


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
