import os

from flask import Flask
from flask import abort, jsonify
from flask import request
from flask import send_file
from initial_db import *
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# @app.route('/matches/<int:match_id>/users', methods=['GET'])
# def get_match_participants(match_id):
#     user = [user for user in users if user['id'] == match_id]
#     if len(user) == 0:
#         abort(404)
#     return jsonify(user[0])


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
        'authorId': request.json.get('authorId'),
        'latLng': {'latitude': request.json.get('latLng')['latitude'],
                   'longitude': request.json.get('latLng')['longitude']},
        'title': request.json.get('title'),
        'date': request.json.get('date'),
        'limit': request.json.get('limit'),
        'id': 0 if not matches else max(matches, key=lambda x: x['id'])['id'] + 1
    }

    matches.append(match)
    return jsonify(match)


if __name__ == '__main__':
    app.run(threaded=True)
