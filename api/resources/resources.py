from flask_restful import Resource
import requests

from api.common.utils import file_response


ENCODING = 'utf-8'
SCHEMA_URL = 'http://127.0.0.1:8422'
STORE_URL = 'http://127.0.0.1:8423'


class FhirDatatypes(Resource):
    @staticmethod
    def get():
        """Returns CSV list of available database schemas."""

        content = requests.get('{}/datatypes_list.json'.format(
            STORE_URL
        )).content.decode(ENCODING)

        return file_response(content, 'json')


class FhirDatatype(Resource):
    @staticmethod
    def get(resource_name):
        """Returns CSV list of available database schemas."""

        content = requests.get('{}/datatypes/{}.json'.format(
            STORE_URL,
            resource_name
        )).content.decode(ENCODING)

        return file_response(content, 'json')


class FhirResources(Resource):
    @staticmethod
    def get():
        """Returns CSV list of available database schemas."""

        content = requests.get('{}/resource_list.json'.format(
            STORE_URL
        )).content.decode(ENCODING)

        return file_response(content, 'json')


class FhirResource(Resource):
    @staticmethod
    def get(resource_name):
        """Returns CSV list of available database schemas."""

        content = requests.get('{}/fhirResources/{}.json'.format(
            STORE_URL,
            resource_name
        )).content.decode(ENCODING)

        return file_response(content, 'json')


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
