from tracker.models import User, Location
from tracker import db
import datetime
import random
from datetime import time

# makes x amount test users for flask app. X is defined by end user when running program.


def populate_database(no_users):
    for i in range(0, no_users):
        create_data(i)


def create_data(number):
    user_to_create = User(username=f"person-{number}",
                          first="Test",
                          last="User",
                          password="password")

    db.session.add(user_to_create)
    db.session.commit()

    #   create a number of random dates and times for the user (up to 10 locations)
    count = 0
    while random.randrange(10):
        #   specify date range
        start_date = datetime.date(2021, 1, 1)
        end_date = datetime.date(2021, 1, 8)

        #   make random date
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)

        # make random time
        random_time = time(random.randrange(24), random.randrange(60))

        #   generate a random location
        places = ['Max Square', 'Public Pool', 'Granada Theatre', 'Riverside Park', 'Bi-Mart',
                  'Wal-Mart', 'D&B Supply', 'Safeway', 'Anytime Fitness', 'Eastern Oregon University']
        random_value = random.randrange(10)
        random_place = places[random_value]
        random_infection = infections[random_value]

        location_to_create = Location(name=random_place,
                                      date=random_date,
                                      time=random_time,
                                      infection=random_infection,
                                      owner=user_to_create.id)
        db.session.add(location_to_create)
        db.session.commit()


print("How many test users do you want to create?")
no_users = input()
infections = [random.randrange(101), random.randrange(101), random.randrange(101), random.randrange(101),
              random.randrange(101), random.randrange(101), random.randrange(101), random.randrange(101),
              random.randrange(101), random.randrange(101)]
print(f"Creating {no_users} users. Please wait...")
populate_database(int(no_users))
print("Finished!")
