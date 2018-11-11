from flask import Flask, jsonify
from flask_restful import Api

from api.resources import Mapping, Store, Schemas


app = Flask(__name__)
api = Api(app)

api.add_resource(Mapping, '/mapping')
api.add_resource(Store, '/store')
api.add_resource(Schemas, '/schemas/<string:database_name>/<string:extension>')


@app.route('/')
def index():
    return jsonify({
        'message': 'Welcome to Fhir API',
    })


if __name__ == '__main__':
    app.run(debug=True)
