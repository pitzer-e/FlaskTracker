from tracker.models import User, Location
from tracker import db
from tracker.models import User

# cleans users with first name "Test." Problem with program, if a user with first name


def clean_database():
    db.drop_all()
    db.create_all()
    admin = User(username='admin',
                 first='super',
                 last='duper',
                 password='password')
    db.session.add(admin)
    db.session.commit()


clean_database()
