from flask import Flask, jsonify
from flask_restful import Api
import json

from api.resources import Mapping, Schemas, Store


app = Flask(__name__)
api = Api(app)

api.add_resource(Mapping, '/mapping')
api.add_resource(Schemas,
    '/schemas/<database_name>/<extension>',
    '/schemas/list',
)
# api.add_resource(Schemas, '/schemas')
api.add_resource(Store, '/store')


if __name__ == '__main__':
    app.run(debug=True)
