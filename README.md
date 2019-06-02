# hydra-openapi-parser
This library contains the OpenAPI parser implemntaion in Python to be used with `hydrus` and `hydra-python-agent`.

Currently the library consists of openapi_parser module which helps hydrus parse OpenAPI standard docs.

To install the library:

```bash
pip install git+https://github.com/HTTP-APIs/hydra-openapi-parser.git#egg=hydra_openapi_parser
```

Note :- If using hydrus, the library doesn't need to be installed separately as it is already a part of requirements.txt for hydrus.
Usage

To import the modules:

```python3
from hydra_openapi_parser import openapi_parser
```

Porting out from hydrus the hydraspecs directory

## Sample use-cases of openapi_parser module

Once the OpenAPI YAML document has been loaded into the program a python dictionary `doc`, you can do the following:
- Parse the OpenAPI doc into a HydraDoc
```python3
parsed_dict = openapi_parser.parse(doc)
```
- Generate an empty object
```python3
object = openapi_parser.generate_empty_object()
```
- Test if an endpoint is valid
```python3
path = 'A/B/{id}/C/D'
openapi_parser.valid_endpoint(path)
# False
path = 'A/B/{id}'
openapi_parser.valid_endpoint(path)
# Collection
path = 'A/B/C'
openapi_parser.valid_endpoint(path)
# True
```
- Extract class name from the path
```python3
path = "A/B/C/Pet"
path_list = path.split('/')
openapi_parser.get_class_name(path_list)
# Pet
```
- Fetch data from location
```python3
path = '#/definitions/Order'
path_list = path.split('/')
data = openapi_parser.get_data_at_location(path_list, doc)
# data is of type dict
```
- Remove variables from path
```python3
path = "A/B/C/{id}"
output = openapi_parser.sanitise_path(path)
```
- Identify if an object is a collection
```python3
schema_block = {
    'type': 'array',
    'items': {
        '$ref': '#/definitions/Pet'
    }
}
method = "/Pet"
openapi_parser.check_collection(schema_block, method)
# True
```
