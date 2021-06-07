from tracker.models import User
from tracker import db

# makes x amount test users for flask app. X is defined by end user when running program.

def populate_database(no_users):
    for i in range(0, no_users):
        user_to_create = create_user(i)
        db.session.add(user_to_create)
        db.session.commit()

""
def create_user(number):
    return User(username=f"person-{number}",
                first="Test",
                last="User",
                password="password")

print("How many test users do you want to create?")
no_users = input()
print(f"Creating {no_users} users. Please wait...")
populate_database(int(no_users))
print("Finished!")
