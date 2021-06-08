from tracker.graph import Graph
from tracker import db
from tracker.models import *
import datetime
from datetime import time, date


def update_infect_chance():
    records = db.session.query(Location).order_by(Location.date).all()
    for record in records:
        print(f"{record.name}: {record.date}")


def gen_report(submitted_location):
    print(f"checking {submitted_location.name}")
    graph = Graph()
    update_infect_chance()
    # pass from date from report page
    python_date = submitted_location.date
    python_time = submitted_location.time
    records = Location.query.filter_by(date=python_date, name=submitted_location.name).all()
    for record in records:
        if record.owner != submitted_location.owner and record.time < python_time:
            print(f"checking against {record.name} from {User.query.filter_by(id=record.owner).first().username}")
            if User.query.filter_by(id=record.owner).first().is_infected or User.query.filter_by(
                    id=record.owner).first().infection_chance > 0:
                print(f"Connecting {record.id} to {submitted_location.id}")
                # add edge between this location and passed location
                graph.add_edge(record.id, submitted_location.id)
                # if record owner is infected
                # then that is the shortest path
                # elif
                # find out who may have infected record owner
