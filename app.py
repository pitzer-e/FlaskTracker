from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/location')
def location_page():
    return render_template('location.html', item_name="Place")


@app.route('/report')
def report_page():
    return render_template('report.html', item_name="Place")
