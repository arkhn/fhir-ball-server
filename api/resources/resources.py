from flask_restful import Resource
import requests

from api.common.utils import file_response


ENCODING = 'utf-8'
MAPPING_URL = 'http://127.0.0.1:8421'
SCHEMA_URL = 'http://127.0.0.1:8422'
STORE_URL = 'http://127.0.0.1:8423'


class Mapping(Resource):
    @staticmethod
    def get(database_name, resource_name, extension):
        """Fetches distant file from Mapping and parses it according to its extension."""

        content = requests.get('{}/{}/{}.{}'.format(
            MAPPING_URL,
            database_name,
            resource_name,
            extension
        )).content.decode(ENCODING)

        return file_response(content, extension)


class Schemas(Resource):
    @staticmethod
    def get():
        """Returns CSV list of available database schemas."""

        content = requests.get('{}/databases.json'.format(
            SCHEMA_URL
        )).content.decode(ENCODING)

        return file_response(content, 'json')


class Schema(Resource):
    @staticmethod
    def get(database_name, extension):
        """Fetches distant file and parses it according to its extension."""

        content = requests.get('{}/{}.{}'.format(
            SCHEMA_URL,
            database_name,
            extension
        )).content.decode(ENCODING)

        return file_response(content, extension)


class Store(Resource):
    @staticmethod
    def get(resource_name, extension):
        """Fetches distant file from Store and parses it according to its extension."""

        content = requests.get('{}/{}.{}'.format(
            STORE_URL,
            resource_name,
            extension
        )).content.decode(ENCODING)

        return file_response(content, extension)
