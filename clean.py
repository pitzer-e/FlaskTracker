from tracker.models import User, Location
from tracker import db

# cleans users with first name "Test." Problem with program, if a user with first name


def clean_database():
    while User.query.filter_by(first="Test").first():
        user = User.query.filter_by(first="Test").first()
        location = Location.query.filter_by(owner=user.id).first()
        db.session.delete(user)
        db.session.delete(location)
    db.session.commit()


clean_database()
