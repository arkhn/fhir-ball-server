from flask import Flask, jsonify
from flask_restful import Api
import json

from api.resources import Mapping, Schema, Schemas, Store


app = Flask(__name__)
api = Api(app)

api.add_resource(Mapping, '/mapping/<database_name>/<resource_name>/<extension>')
api.add_resource(Schema, '/schema/<database_name>/<extension>')
api.add_resource(Schemas, '/schemas')
api.add_resource(Store, '/store/<resource_name>')


if __name__ == '__main__':
    app.run(debug=True)
