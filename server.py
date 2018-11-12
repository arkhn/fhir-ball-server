from flask import Flask
from flask_restful import Api

from api.resources import FhirDatatypes, FhirResource, FhirResources, Schema, Schemas


app = Flask(__name__)
api = Api(app)

api.add_resource(FhirDatatypes, '/fhir_datatypes')
api.add_resource(FhirResource, '/fhir_resource/<resource_name>')
api.add_resource(FhirResources, '/fhir_resources')
api.add_resource(Schema, '/schema/<database_name>/<extension>')
api.add_resource(Schemas, '/schemas')


if __name__ == '__main__':
    app.run(debug=True)
