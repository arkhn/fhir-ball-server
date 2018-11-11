from flask import jsonify, make_response, send_from_directory
# note: prefer send_from_directory to send_file  as send_file is not secured.
# From the official documentation : "Please never pass filenames to this function from user sources;
# you should use send_from_directory() instead."
from flask_restful import Resource, reqparse
import json
import os
import requests
import yaml


MAPPING_URL = 'http://127.0.0.1:8421'
SCHEMA_URL = 'http://127.0.0.1:8422'
STORE_URL = 'http://127.0.0.1:8423'


class Mapping(Resource):
    def get(self, database_name, resource_name, extension):
        '''Fetches distant file and parses it according to its extension.'''

        content = requests.get('{}/{}/{}.{}'.format(
            MAPPING_URL,
            database_name,
            resource_name,
            extension
        )).content

        if extension == 'json':
            return jsonify(json.loads(content))
        elif extension == 'yml':
            return jsonify(yaml.load(content))

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
    def get(self, resource_name):
        content = requests.get('{}/{}.{}'.format(
            STORE_URL,
            resource_name,
            extension
        )).content

        if extension == 'json':
            return jsonify(json.loads(content))
        elif extension == 'yml':
            return jsonify(yaml.load(content))

        return jsonify({
            'message': 'Extension not found.'
        })
