import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS
import pymongo

# Configuration
DEBUG = True

# Initialize app
app = Flask(__name__)
app.config.from_object(__name__)

# Mongodb connection initialization to database gameStore
db = pymongo.MongoClient("mongodb://datinguser:datinguserpasswd@mongodb:27017/")['gameStore']

# Enable CORS (CORS is a library that enables cross-origin requests)
# For example different protocol, IP address, domain name or port
CORS(app, resources={r'/*': {'origins': '*'}})


# Sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


# Routing
@app.route('/admin', methods=['GET', 'POST'])
def all_games():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()

        # Inserting to games collection
        db['games'].insert({
            '_id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'developer': db['developers'].find_one({'name': post_data.get('developer')})['_id'],
            'publisher': db['publishers'].find_one({'name': post_data.get('publisher')})['_id'],
            'genre': db['genres'].find_one(({'name': post_data.get('genre')}))['_id']
        })

        response_object['message'] = 'Game added!'

    else:
        query = []

        # Getting all the games from the games collection (like SELECT * FROM games)
        for game in db['games'].find():
            query.append({
                'id': game['_id'],
                'title': game['title'],
                'developer': db['developers'].find_one({'_id': game['developer']})['name'],
                'publisher': db['publishers'].find_one({'_id': game['publisher']})['name'],
                'genre': db['genres'].find_one({'_id': game['genre']})['name']
            })

        response_object['games'] = query

    return jsonify(response_object)


@app.route('/admin/<game_id>', methods=['PUT', 'DELETE'])
def single_game(game_id):
    response_object = {'status': 'success'}

    if request.method == 'PUT':
        post_data = request.get_json()

        # Updating one game (like ALTER TABLE games WHERE _id = game_id);
        db['games'].update_one({"_id": game_id}, {
            'title': post_data.get('title'),
            'developer': db['developers'].find_one({'_id': post_data.get('developer')})['name'],
            'publisher': db['publishers'].find_one({'_id': post_data.get('publisher')})['name'],
            'genre': db['genres'].find_one({'_id': post_data.get('genre')})['name']
        })

        response_object['message'] = 'Game updated!'

    if request.method == 'DELETE':
        db['games'].delete_one({'_id': game_id})
        response_object['message'] = 'Game removed!'

    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
