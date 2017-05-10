import datetime
import time

_s = "01/12/2011"
_sample_date = time.mktime(datetime.datetime.strptime(_s, "%d/%m/%Y").timetuple())
users = [
    {'id': 1, 'name': 'Jerzy'},
    {'id': 2, 'name': 'Marian'},
    {'id': 3, 'name': 'Grzegorz'},
    {'id': 4, 'name': 'Franciszek'},
    {'id': 5, 'name': 'Ireneusz'},
    {'id': 6, 'name': 'Romuald'}
]

matches = [
    # {
    #     'id': 1,
    #     'title': "asdfadfgsdfg",
    #     'date': _sample_date,
    #     'participants': [1, 2]
    # },
    # {
    #     'id': 2,
    #     'title': "456wtry",
    #     'date': _sample_date,
    #     'participants': [1, 3, 4, 2]
    # },
    # {
    #     'id': 3,
    #     'title': "po;'0;il;",
    #     'date': _sample_date,
    #     'participants': [4, 2]
    # },
    # {
    #     'id': 4,
    #     'title': "hkjghkhjk",
    #     'date': _sample_date,
    #     'participants': []
    # },
    # {
    #     'id': 5,
    #     'title': "q345324",
    #     'date': _sample_date,
    #     'participants': [1, 3]
    # }
]
