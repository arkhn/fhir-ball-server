[![GitHub license](https://img.shields.io/github/license/arkhn/fhir-pipe.svg)](https://github.com/arkhn/fhir-pipe/blob/master/LICENSE)
[![Website arkhn.org](https://img.shields.io/website-up-down-green-red/https/arkhn.org.svg)](http://arkhn.org/)

# Fhirball Server

This is a RESTful API to serve data to the client. It is mainly routes requests to back-ends running on the same machine which respectively contain and serve all needed data.

## Installation

Python modules should be installed first: `pip install requirements.txt`. This file was generated unsing `pipreqs --force ./`.

## Usage

In order to start the server in a development environment, run the following command:
```
FLASK_ENV=development python3 ./server.py
```

Otherwise, run:
```
python3 ./server.py
```

## Available resources

### Schemas

* `[url]/schemas` returns a CSV list of available database schemas.
* `[url]/schema/<database_name>/<extension>` returns a file containing the schema of a given database.

### Store

Requests should be sent to `[ur]/store`.
The body of your request must match the following template:

```
{
	"output_format": "json",
	"fhir_resource_name": "patient",
}
```

### Mapping

Requests should be sent to `[url]/mapping`.
The body of your request must match the following template:
```
{
	"output_format": "json",
	"fhir_resource_name": "patient",
	"database": "CW,"
}
```
