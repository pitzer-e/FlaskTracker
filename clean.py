from tracker.models import User
from tracker import db

# cleans users with first name "Test." Problem with program, if a user with first name

def clean_database():
    while User.query.filter_by(first="Test").first():
        db.session.delete(User.query.filter_by(first="Test").first())
    db.session.commit()

clean_database()