from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '3ec7142bf14425b34e3e3746'
db = SQLAlchemy(app)

#   This import is required at the end of the file. It prevents circular calling and provides context for routes.
from tracker import routes
