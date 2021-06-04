from tracker import db, login_manager
from tracker import bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    first = db.Column(db.String(length=30), nullable=False)
    last = db.Column(db.String(length=30), nullable=False)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    is_infected = db.Column(db.Boolean(), nullable=False, default=False)
    id = db.Column(db.Integer(), primary_key=True)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Location(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    infection = db.Column(db.Float(), nullable=False, default=0.0)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))


class Date(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    datetime = db.Column(db.Date(), default='2020-01-01 12:00')
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
