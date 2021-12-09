"""
Generated API Documentation for Server API using
                server_doc_gen.py."""

doc = {
    "@context": {
        "ApiDocumentation": "hydra:ApiDocumentation",
        "description": "hydra:description",
        "domain": {
            "@id": "rdfs:domain",
            "@type": "@id"
        },
        "entrypoint": {
            "@id": "hydra:entrypoint",
            "@type": "@id"
        },
        "expects": {
            "@id": "hydra:expects",
            "@type": "@id"
        },
        "expectsHeader": "hydra:expectsHeader",
        "hydra": "http://www.w3.org/ns/hydra/core#",
        "label": "rdfs:label",
        "manages": "hydra:manages",
        "method": "hydra:method",
        "object": {
            "@id": "hydra:object",
            "@type": "@id"
        },
        "possibleStatus": "hydra:possibleStatus",
        "property": {
            "@id": "hydra:property",
            "@type": "@id"
        },
        "range": {
            "@id": "rdfs:range",
            "@type": "@id"
        },
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "readable": "hydra:readable",
        "required": "hydra:required",
        "returns": {
            "@id": "hydra:returns",
            "@type": "@id"
        },
        "returnsHeader": "hydra:returnsHeader",
        "search": "hydra:search",
        "statusCode": "hydra:statusCode",
        "subClassOf": {
            "@id": "rdfs:subClassOf",
            "@type": "@id"
        },
        "subject": {
            "@id": "hydra:subject",
            "@type": "@id"
        },
        "supportedClass": "hydra:supportedClass",
        "supportedOperation": "hydra:supportedOperation",
        "supportedProperty": "hydra:supportedProperty",
        "title": "hydra:title",
        "writeable": "hydra:writeable",
        "xsd": "https://www.w3.org/TR/xmlschema-2/#"
    },
    "@id": "http://petstore.swagger.io/api/v1/vocab",
    "@type": "ApiDocumentation",
    "description": "A sample API that uses a petstore as an example to demonstrate features in the OpenAPI 3.0 specification",
    "entrypoint": "http://petstore.swagger.io/api/v1",
    "possibleStatus": [],
    "supportedClass": [
        {
            "@id": "http://petstore.swagger.io/api/v1/vocab",
            "@type": "hydra:Class",
            "description": "Class for Pet",
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/Integer",
                    "readable": "false",
                    "required": "true",
                    "title": "id",
                    "writeable": "false"
                }
            ],
            "title": "Pet"
        },
        {
            "@id": "http://petstore.swagger.io/api/v1/vocab",
            "@type": "hydra:Class",
            "description": "Class for NewPet",
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/Text",
                    "readable": "false",
                    "required": "true",
                    "title": "name",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/Text",
                    "readable": "false",
                    "required": "true",
                    "title": "tag",
                    "writeable": "false"
                }
            ],
            "title": "NewPet"
        },
        {
            "@id": "http://petstore.swagger.io/api/v1/vocab",
            "@type": "hydra:Class",
            "description": "Class for Error",
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/Integer",
                    "readable": "false",
                    "required": "true",
                    "title": "code",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/Text",
                    "readable": "false",
                    "required": "true",
                    "title": "message",
                    "writeable": "false"
                }
            ],
            "title": "Error"
        },
        {
            "@id": "http://petstore.swagger.io/api/v1/vocab",
            "@type": "hydra:Class",
            "description": "Class for Pets",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "http://petstore.swagger.io/api/v1/vocab?resource=Pets",
                    "expectsHeader": [],
                    "method": "POST",
                    "possibleStatus": [
                        {
                            "@context": "https://www.w3.org/ns/hydra/core",
                            "@type": "Status",
                            "description": "pet response",
                            "statusCode": 200,
                            "title": ""
                        },
                        {
                            "@context": "https://www.w3.org/ns/hydra/core",
                            "@type": "Status",
                            "description": "unexpected error",
                            "statusCode": 500,
                            "title": ""
                        }
                    ],
                    "returns": "http://petstore.swagger.io/api/v1/vocab?resource=Pets",
                    "returnsHeader": [],
                    "title": "addPet"
                },
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "",
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "@context": "https://www.w3.org/ns/hydra/core",
                            "@type": "Status",
                            "description": "pet response",
                            "statusCode": 200,
                            "title": ""
                        },
                        {
                            "@context": "https://www.w3.org/ns/hydra/core",
                            "@type": "Status",
                            "description": "unexpected error",
                            "statusCode": 500,
                            "title": ""
                        }
                    ],
                    "returns": "http://petstore.swagger.io/api/v1/vocab?resource=Pets",
                    "returnsHeader": [],
                    "title": "find pet by id"
                },
                {
                    "@type": "http://schema.org/DeleteAction",
                    "expects": "",
                    "expectsHeader": [],
                    "method": "DELETE",
                    "possibleStatus": [
                        {
                            "@context": "https://www.w3.org/ns/hydra/core",
                            "@type": "Status",
                            "description": "pet deleted",
                            "statusCode": 204,
                            "title": ""
                        },
                        {
                            "@context": "https://www.w3.org/ns/hydra/core",
                            "@type": "Status",
                            "description": "unexpected error",
                            "statusCode": 500,
                            "title": ""
                        }
                    ],
                    "returns": "",
                    "returnsHeader": [],
                    "title": "deletePet"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/Integer",
                    "readable": "false",
                    "required": "true",
                    "title": "id",
                    "writeable": "false"
                }
            ],
            "title": "Pets"
        },
        {
            "@id": "http://www.w3.org/ns/hydra/core#Collection",
            "@type": "hydra:Class",
            "description": "null",
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": "false",
                    "required": "null",
                    "title": "members",
                    "writeable": "false"
                }
            ],
            "title": "Collection"
        },
        {
            "@id": "http://www.w3.org/ns/hydra/core#Resource",
            "@type": "hydra:Class",
            "description": "null",
            "supportedOperation": [],
            "supportedProperty": [],
            "title": "Resource"
        },
        {
            "@id": "http://petstore.swagger.io/api/v1/vocab?resource=PetsCollection",
            "@type": "Collection",
            "description": "A collection for pets",
            "manages": {
                "object": "http://petstore.swagger.io/api/v1/vocab?resource=Pets",
                "property": "rdfs:type"
            },
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:PetsCollection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all the members of PetsCollection",
                    "expects": "null",
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "http://petstore.swagger.io/api/v1/vocab?resource=Pets",
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The members of PetsCollection",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": "true",
                    "required": "false",
                    "title": "members",
                    "writeable": "true"
                }
            ],
            "title": "PetsCollection"
        },
        {
            "@id": "http://petstore.swagger.io/api/v1#EntryPoint",
            "@type": "hydra:Class",
            "description": "The main entry point or homepage of the API.",
            "supportedOperation": [
                {
                    "@id": "_:entry_point",
                    "@type": "http://petstore.swagger.io/http://petstore.swagger.io/api/v1#EntryPoint",
                    "description": "The APIs main entry point.",
                    "expects": "null",
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "null",
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [],
            "title": "EntryPoint"
        }
    ],
    "title": "Swagger Petstore"
}
