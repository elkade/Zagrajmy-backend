from flask import Flask
from flask import abort, jsonify
import datetime
import time

from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


s = "01/12/2011"

matches = [
    {'id': 1, 'title': "asdfadfgsdfg", 'date': time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())},
    {'id': 2, 'title': "456wtry", 'date': time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())},
    {'id': 3, 'title': "po;'0;il;", 'date': time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())},
    {'id': 4, 'title': "hkjghkhjk", 'date': time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())},
    {'id': 5, 'title': "q345324", 'date': time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())}
]


@app.route('/matches/<int:match_id>', methods=['GET'])
def get_match(match_id):
    match = [match for match in matches if match['id'] == match_id]
    if len(match) == 0:
        abort(404)
    return jsonify(match[0])


@app.route('/matches', methods=['GET'])
def get_matches():
    return jsonify(matches)


@app.route('/matches', methods=['POST'])
def post_match():
    match = {
        'title': request.json.get('title'),
        'date': request.json.get('date'),
        'id': max(matches, key=lambda x: x['id'])['id'] + 1
    }

    matches.append(match)
    return jsonify(match)


if __name__ == '__main__':
    app.run(threaded=True)
