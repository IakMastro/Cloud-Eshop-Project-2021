import uuid

from flask import Flask, jsonify, request, g
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo

# Configuration
DEBUG = True

# Initialize app
app = Flask(__name__)
app.config.from_object(__name__)

# Mongodb connection initialization to database gameStore'
app.config['MONGO_URI'] = "mongodb://dbuser:dbpass@mongodb:27017/gameStore?authSource=admin"
mongo = PyMongo(app)

# Enable CORS (CORS is a library that enables cross-origin requests)
# For example different protocol, IP address, domain name or port
CORS(app, resources={r'/*': {'origins': '*'}})


# Sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


# Routing
@app.route('/admin', methods=['GET', 'POST'])
@cross_origin()
def all_games():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()

        # Inserting to games collection
        mongo.db.games.insert({
            '_id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'developer': mongo.db.developers.find_one({'name': post_data.get('developer')})['_id'],
            'publisher': mongo.db.publishers.find_one({'name': post_data.get('publisher')})['_id'],
            'genre': mongo.db.genres.find_one(({'name': post_data.get('genre')}))['_id']
        })

        response_object['message'] = 'Game added!'

    else:
        query = []

        # Getting all the games from the games collection (like SELECT * FROM games)
        for game in mongo.db.games.find():
            query.append({
                'id': game['_id'],
                'title': game['title'],
                'developer': mongo.db.developers.find_one({'_id': game['developer']})['name'],
                'publisher': mongo.db.publishers.find_one({'_id': game['publisher']})['name'],
                'genre': mongo.db.genres.find_one({'_id': game['genre']})['name']
            })

        response_object['games'] = query

    query = jsonify(response_object)
    return query


@app.route('/admin/<game_id>', methods=['PUT', 'DELETE'])
@cross_origin()
def single_game(game_id):
    response_object = {'status': 'success'}

    if request.method == 'PUT':
        post_data = request.get_json()

        # Updating one game (like ALTER TABLE games WHERE _id = game_id);
        mongo.db.games.update_one({"_id": game_id}, {
            'title': post_data.get('title'),
            'developer': mongo.db.developers.find_one({'_id': post_data.get('developer')})['name'],
            'publisher': mongo.db.publishers.find_one({'_id': post_data.get('publisher')})['name'],
            'genre': mongo.db.genres.find_one({'_id': post_data.get('genre')})['name']
        })

        response_object['message'] = 'Game updated!'

    if request.method == 'DELETE':
        mongo.db.games.delete_one({'_id': game_id})
        response_object['message'] = 'Game removed!'

    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
