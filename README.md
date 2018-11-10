# API

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
