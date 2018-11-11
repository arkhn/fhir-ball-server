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


class Mapping(Resource):
    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('output_format', required=True, type=str, choices=('json', 'yml'))
        parser.add_argument('fhir_resource_name', required=True, type=str)
        parser.add_argument('database', required=True, type=str)

        args = parser.args()

        file_path = fhir_resource_path(args['fhir_resource_name'], parent_folder=args['database'])
        if not file_path:
            return jsonify(
                {"message": "Fhir resource not found."}
            )

        folder = os.path.dirname(file_path)
        file = os.path.basename(file_path)

        if args['output_format'] == 'json':
            return jsonify(yaml.load(open(file_path)))

        elif args['output_format'] == 'yml':
            return send_from_directory(folder, file)


class Schemas(Resource):
    '''
    Restful API dealing with databases schemas.
    '''

    def __init__(self):
        '''
        Inits instance parameters.
        '''

        self.url = 'http://127.0.0.1:8421'

    def get(self, **kwargs):
        '''
        Calls resource's method depending on the number
        of arguemnts.
        '''

        if len(kwargs) == 0:
            return self.get_list()
        elif len(kwargs) == 2:
            return self.get_schema(**kwargs)

        return jsonify({
            'message': 'Invalid number of arguments',
        })

    def get_list(self):
        '''
        Fetches CSV from distant source and builds
        a flask response.
        '''

        content = requests.get('{}/databases.csv'.format(
            self.url
        )).content

        response = make_response(content)
        cd = 'attachment; filename=databases.csv'
        response.headers['Content-Disposition'] = cd
        response.mimetype = 'text/csv'

        return response

    def get_schema(self, database_name, extension):
        '''
        Fetches distant file and parses it according
        to its extension.
        '''

        content = requests.get('{}/{}.{}'.format(
            self.url,
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
            return jsonify(
                {"message": "Fhir resource not found."}
            )

        folder = os.path.dirname(file_path)
        file = os.path.basename(file_path)
        if args['output_format'] == 'json':
            return jsonify(yaml.load(open(file_path)))

        elif args['output_format'] == 'yml':
            return send_from_directory(folder, file)
