import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo

# Configuration
DEBUG = True

# Initialize app
app = Flask(__name__)
app.config.from_object(__name__)

# Mongodb connection initialization to database gameStore
app.config['MONGO_URI'] = "mongodb://datinguser:datinguserpasswd@mongodb:27017/gameStore?authSource=admin"
mongo = PyMongo(app)

# Initialize CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/login', methods=['PUT'])
def login():
    response_object = {'status': 'success'}
    post_data = request.get_json()

    # Getting all the users from the database
    for user in mongo.db.users.find():
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


@app.route('/signup', methods=['POST'])
def signup():
    response_object = {'status': 'success'}
    post_data = request.get_json()

    if mongo.db.users.find_one({'username': post_data.get('username')}) is None:
        # Inserting new user to database
        mongo.db.users.insert({
            '_id': uuid.uuid4().hex,
            'username': post_data.get('username'),
            'password': post_data.get('password'),
            'admin': False,
            'games_owned': {}
        })

        response_object['message'] = 'User made!'

    else:
        response_object['message'] = 'Username already exists'

    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
