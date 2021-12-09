from hydra_python_core.doc_writer import HydraClassProp, HydraCollection, HydraClass
from exceptions import HydraCollectionException
from processors.api_info_processor import APIInfoProcessor
from processors.class_processor import ClassProcessor
from processors.collection_processor import CollectionProcessor
from processors.prop_processor import PropertyProcessor
from parsers.ref_parser import RefParser
from utils import type_ref_mapping
from typing import Dict, List, Union, Any


class SchemaParser:
    def __init__(self, schema_details: Dict[str, Any]) -> None:
        self.schema_details = schema_details
        self.id = APIInfoProcessor.api_info["id"]

    @staticmethod
    def create_props(title, property_details, required=False):
        if property_details.get("type") == "array":
            raise HydraCollectionException("Property contains a hydra collection.")
        prop = type_ref_mapping(property_details["type"])
        property_processor = PropertyProcessor(prop, title, required)
        hydra_prop = property_processor.generate()
        return hydra_prop

    @staticmethod
    def parse_props(schema_definition):
        props = {}
        if schema_definition.get("required"):
            for required_prop in schema_definition.get("required"):
                property_details = schema_definition.get("properties")[required_prop]
                props[required_prop] = SchemaParser.create_props(
                    required_prop, property_details, True
                )
        if schema_definition.get("properties"):
            for prop in schema_definition.get("properties"):
                if props.get(prop):
                    continue
                property_details = schema_definition.get("properties")[prop]
                props[prop] = SchemaParser.create_props(prop, property_details, True)
        return list(props.values())

    @staticmethod
    def get_props(schema_definition):
        hydra_class_props = []
        for key, value in schema_definition.items():
            if key in ["allOf", "anyOf", "oneOf"]:
                for schema_definition_ in value:
                    hydra_class_props.extend(SchemaParser.get_props(schema_definition_))
            else:
                if schema_definition.get("$ref"):
                    pass
                    # ref_parser = RefParser(value)
                    # hydra_class = ref_parser.parse()
                elif schema_definition.get("type") == "array":
                    raise HydraCollectionException("Schema contains hydra collection")
                else:
                    return SchemaParser.parse_props(schema_definition)
        return hydra_class_props

    def parse(self) -> List[List[Union[HydraClass, HydraCollection]]]:
        hydra_classes = {}
        hydra_collections = {}
        for name, definition in self.schema_details.items():
            # schmas containing refs
            if name == "$ref":
                ref_parser = RefParser(definition)
                hydra_class, hydra_collection = ref_parser.parse()
                if hydra_class:
                    hydra_classes[hydra_class.__dict__.get("title")] = hydra_class
                if hydra_collection:
                    hydra_collections[
                        hydra_collection.__dict__.get("title")
                    ] = hydra_collection
            else:
                # for schemas defined in the paramters/responses
                if name in ["type", "properties", "required"]:
                    definition = self.schema_details
                try:
                    hydra_props = SchemaParser.get_props(definition)
                    class_processor = ClassProcessor(
                        title=name, id=self.id, hydra_props=hydra_props
                    )
                    hydra_class = class_processor.generate()
                    hydra_classes[name] = hydra_class
                except HydraCollectionException:
                    collection_processor = CollectionProcessor(title=name, id=self.id)
                    hydra_collection = collection_processor.generate()
                    hydra_collections[name] = hydra_collection
        return [hydra_classes, hydra_collections]
