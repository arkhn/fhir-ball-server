from flask import jsonify, make_response, send_from_directory
# note: prefer send_from_directory to send_file  as send_file is not secured.
# From the official documentation : "Please never pass filenames to this function from user sources;
# you should use send_from_directory() instead."
from flask_restful import Resource, reqparse
import json
import os
import requests
import yaml

from api.common.utils import fhir_resource_path


SCHEMA_URL = 'http://127.0.0.1:8421'


class Mapping(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('output_format', required=True, type=str, choices=('json', 'yml'))
        parser.add_argument('fhir_resource_name', required=True, type=str)
        parser.add_argument('database', required=True, type=str)

        args = parser.args()

        file_path = fhir_resource_path(args['fhir_resource_name'], parent_folder=args['database'])

        if not file_path:
            return jsonify({
                "message": "Fhir resource not found.",
            })

        folder = os.path.dirname(file_path)
        file = os.path.basename(file_path)

        if args['output_format'] == 'json':
            return jsonify(yaml.load(open(file_path)))
        elif args['output_format'] == 'yml':
            return send_from_directory(folder, file)

        return jsonify({
            'message': 'Extension not found.'
        })


class Schemas(Resource):
    def get(self):
        '''Returns CSV list of available database schemas.'''

        content = requests.get('{}/databases.csv'.format(
            SCHEMA_URL
        )).content

        response = make_response(content)
        response.headers['Content-Disposition'] = 'attachment; filename=databases.csv'
        response.mimetype = 'text/csv'

        return response


class Schema(Resource):
    def get(self, database_name, extension):
        '''Fetches distant file and parses it according to its extension.'''

        content = requests.get('{}/{}.{}'.format(
            SCHEMA_URL,
            database_name,
            extension
        )).content

        if extension == 'json':
            return jsonify(json.loads(content))
        elif extension == 'yml':
            return jsonify(yaml.load(content))

        return jsonify({
            'message': 'Unknown extension.'
        })


class Store(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('output_format', required=True, type=str, choices=('json', 'yml'))
        parser.add_argument('fhir_resource_name', required=True, type=str)

        args = parser.parse_args()

        file_path = fhir_resource_path(args['fhir_resource_name'], parent_folder=args['output_format'])

        if not file_path:
            return jsonify({
                "message": "Fhir resource not found."
            })

        folder = os.path.dirname(file_path)
        file = os.path.basename(file_path)

        if args['output_format'] == 'json':
            return jsonify(yaml.load(open(file_path)))
        elif args['output_format'] == 'yml':
            return send_from_directory(folder, file)

        return jsonify({
            'message': 'Extension not found.',
        })
