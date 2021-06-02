from tracker import db


class User(db.Model):
    first_name = db.Column(db.String(length=30), nullable=False)
    last_name = db.Column(db.String(length=30), nullable=False)
    user_name = db.Column(db.String(length=30), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    is_infected = db.Column(db.Boolean(), nullable=False, default=False)
    user_id = db.Column(db.Integer(), primary_key=True)


class Location(db.Model):
    location_id = db.Column(db.Integer(), primary_key=True)
    location_name = db.Column(db.String(length=30), nullable=False, unique=True)
    location_addr = db.Column(db.String(length=30), nullable=False, unique=True)
    location_infection = db.Column(db.Float(), nullable=False)


class Date(db.Model):
    create_day = db.Column(db.Date(), nullable=False, default=db.Date(), primary_key=True)
    create_time = db.Column(db.Time(), default=db.Time(), nullable=False)
