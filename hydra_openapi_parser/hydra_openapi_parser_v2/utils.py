from hydra_python_core.doc_writer import HydraDoc
import json
from typing import Dict, Any, List


def parser_class_mapping(category):
    from parsers.param_parser import ParameterParser
    from parsers.resp_parser import ResponseParser
    from parsers.path_parser import PathParser
    from parsers.method_parser import MethodParser
    from parsers.schema_parser import SchemaParser

    parser_class_mapping = dict()
    parser_class_mapping = {
        "path": PathParser,
        "response": ResponseParser,
        "parameter": ParameterParser,
        "method": MethodParser,
        "schema": SchemaParser,
    }
    return parser_class_mapping[category]


def component_class_mapping(component):
    from parsers.param_parser import ParameterParser
    from parsers.schema_parser import SchemaParser
    from parsers.resp_parser import ResponseParser

    components = dict()
    components = {
        "schemas": SchemaParser,
        "parameters": ParameterParser,
        "responses": ResponseParser,
        "securitySchemes": "",
        "requestBodies": "",
        "headers": "",
        "examples": "",
        "links": "",
        "callbacks": "",
    }
    return components[component]


def type_ref_mapping(type: str) -> str:
    """
    Returns semantic ref for OAS data types
    :param type: data type
    :return: ref
    """
    dataType_ref_map = dict()
    # todo add support for byte , binary , password ,double data types
    dataType_ref_map["integer"] = "https://schema.org/Integer"
    dataType_ref_map["string"] = "https://schema.org/Text"
    dataType_ref_map["long"] = "http://books.xmlschemata.org/relaxng/ch19-77199.html"
    dataType_ref_map["float"] = "https://schema.org/Float"
    dataType_ref_map["boolean"] = "https://schema.org/Boolean"
    dataType_ref_map["dateTime"] = "https://schema.org/DateTime"
    dataType_ref_map["date"] = "https://schema.org/Date"

    return dataType_ref_map[type]


def gen_entrypoint(api_doc: HydraDoc) -> HydraDoc:
    """
    Generates Entrypoint, Base Collection and Base Resource for the documentation
    :param api_doc: contains the Hydra Doc created
    """
    api_doc.add_baseCollection()
    api_doc.add_baseResource()
    api_doc.gen_EntryPoint()
    return api_doc


def gen_doc_file(hydra_doc: Dict[str, Any]) -> str:
    """
    Helper function to dump generated hydradoc > py file.
    :param doc: generated hydra doc
    :return:  hydra doc created
    """
    dump = json.dumps(hydra_doc, indent=4, sort_keys=True)
    hydra_doc = '''"""\nGenerated API Documentation for Server API using
                server_doc_gen.py."""\n\ndoc = {}'''.format(
        dump
    )
    hydra_doc = "{}\n".format(hydra_doc)
    hydra_doc = hydra_doc.replace("true", '"true"')
    hydra_doc = hydra_doc.replace("false", '"false"')
    hydra_doc = hydra_doc.replace("null", '"null"')

    return hydra_doc
