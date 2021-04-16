import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS

# Configuration
DEBUG = True

# Initialize app
app = Flask(__name__)
app.config.from_object(__name__)

# Enable CORS (CORS is a library that enables cross-origin requests)
# For example different protocol, IP address, domain name or port
CORS(app, resources={r'/*': {'origins': '*'}})

GAMES = [
    {
        'id': uuid.uuid4().hex,
        'title': 'Metal Gear Solid 3: Snake Eater',
        'developer': 'Kojima',
        'favoured': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Yakuza 0',
        'developer': 'Ryu Ga Gotoku Studios',
        'favoured': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Call Of Duty: Modern Warfare (2019)',
        'developer': 'Infinity Ward',
        'favoured': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Persona 4 Golden Edition',
        'developer': 'Atlus',
        'favoured': True
    },
]


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

        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'developer': post_data.get('developer'),
            'favoured': post_data.get('favoured'),
        })

        response_object['message'] = 'Game added!'

    else:
        response_object['games'] = GAMES

    return jsonify(response_object)


def remove_game(game_id):
    for game in GAMES:
        if game['id'] == game_id:
            GAMES.remove(game)
            return True

    return False


@app.route('/admin/<game_id>', methods=['PUT', 'DELETE'])
def single_game(game_id):
    response_object = {'status': 'success'}

    if request.method == 'PUT':
        post_data = request.get_json()
        remove_game(game_id)

        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'developer': post_data.get('developer'),
            'favoured': post_data.get('favoured')
        })

        response_object['message'] = 'Game updated!'

    if request.method == 'DELETE':
        remove_game(game_id)
        response_object['message'] = 'Game removed!'

    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
