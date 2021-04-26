import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS

# Configuration
DEBUG = True

# Initialize app
app = Flask(__name__)
app.config.from_object(__name__)

# Initialize CORS
CORS(app, resource={r'/*': {'origins': '*'}})

USERS = [
    {
        'id': uuid.uuid4().hex,
        'username': 'admin',
        'password': 'pass',
        'admin': True
    },
    {
        'id': uuid.uuid4().hex,
        'username': 'foo',
        'password': 'bar',
        'admin': False
    },
]


@app.route('/library', methods=['PUT'])
def library():
    response_object = {'status': 'success'}
    post_data = request.get_json()

    for user in USERS:
        if post_data['username'] == user['username']:
            if post_data['password'] == user['password']:
                response_object['message'] = 'Logged in successfully'
                response_object['user'] = user
                return jsonify(response_object)

            else:
                response_object['message'] = 'Wrong password! Try again...'
                return jsonify(response_object)

    response_object['message'] = 'Username is wrong.'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run(port=5001)
