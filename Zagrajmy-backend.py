import os

from flask import Flask
from flask import abort, jsonify
import datetime
import time

from flask import flash
from flask import request
from flask import send_file

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


s = "01/12/2011"

users = [
    {'id': 1, 'name': 'Jerzy'},
    {'id': 2, 'name': 'Marian'},
    {'id': 3, 'name': 'Grzegorz'},
    {'id': 4, 'name': 'Franciszek'}
]

matches = [
    {'id': 1, 'title': "asdfadfgsdfg", 'date': time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())},
    {'id': 2, 'title': "456wtry", 'date': time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())},
    {'id': 3, 'title': "po;'0;il;", 'date': time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())},
    {'id': 4, 'title': "hkjghkhjk", 'date': time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())},
    {'id': 5, 'title': "q345324", 'date': time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())}
]


@app.route('/images/<int:image_id>', methods=['PUT'])
def put_image(image_id):
    if 'file' not in request.files:
        abort('No file part')
    file = request.files['file']
    extension = os.path.splitext(file.filename)[1]
    f_name = str(image_id)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'images', f_name)
    try:
        os.remove(path)
    except:
        pass
    file.save(path)
    return ('', 204)


@app.route('/images/<int:image_id>', methods=['GET'])
def get_image(image_id):
    try:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'images', str(image_id))
        return send_file(path, mimetype='image/jpeg')
    except:
        abort(404)
    return ('', 204)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    return jsonify(user[0])


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


@app.route('/users', methods=['POST'])
def post_user():
    user = {
        'name': request.json.get('name'),
        'id': max(users, key=lambda x: x['id'])['id'] + 1
    }

    users.append(user)
    return jsonify(user)


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
