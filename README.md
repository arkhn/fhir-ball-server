[![GitHub license](https://img.shields.io/github/license/arkhn/fhir-pipe.svg)](https://github.com/arkhn/fhir-pipe/blob/master/LICENSE)
[![Website arkhn.org](https://img.shields.io/website-up-down-green-red/https/arkhn.org.svg)](http://arkhn.org/)

# Fhirball Server

This is a RESTful API to serve data to the client.

## Usage

### Store

Requests should be sent to: `[ur]/store`
The body of your request must match the following template:

```
{
	"output_format": "json",
	"fhir_resource_name": "patient",
}
```

### Mapping

Requests should be sent to: `[url]/mapping`
The body of your request must match the following template:
```
{
	"output_format": "json",
	"fhir_resource_name": "patient",
	"database": "CW,"
}
```
