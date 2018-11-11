from flask import Flask, jsonify
from flask_restful import Api
import json
import requests

from api.resources import Mapping, Store


app = Flask(__name__)
api = Api(app)

api.add_resource(Mapping, '/mapping')
api.add_resource(Store, '/store')

@app.route('/schemas/<database_name>/<extension>', methods=['GET'])
def get_schema(database_name, extension):

    content = requests.get('http://127.0.0.1:8421/{}.{}'.format(
        database_name, extension
    )).content

    return jsonify(json.loads(content))

@app.route('/')
def index():
    return jsonify({
        'message': 'Welcome to Fhir API',
    })


if __name__ == '__main__':
    app.run(debug=True)
