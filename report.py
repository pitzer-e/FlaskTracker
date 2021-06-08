from graph import Graph
from tracker import db
from tracker.models import *
import datetime
from datetime import time, date

graph = Graph
python_date = date(2021, 1, 13)
python_time = time(6, 0)
records = Location.query.filter_by(date=python_date).all()
for record in records:
    if record.time > python_time:
        print('welldang')

