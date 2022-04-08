from typing import Type
from processors.prop_processor import PropertyProcessor
from utils import type_ref_mapping
from exceptions import ExpectsValueError, HydraCollectionException


class ParameterParser:
    def __init__(self, parameter) -> None:
        self.parameter = parameter

    def parse(self):
        is_collection = False
        prop = "null"
        title = ("null",)
        required = (False,)

        for key, value in self.parameter.items():
            if key == "schema":
                schema = value
                if schema.get("type") == "array":
                    is_collection = True
                else:
                    try:
                        prop = type_ref_mapping(schema.get("type"))
                    except KeyError:
                        raise ExpectsValueError(
                            "{} is incorrect parameter for 'supportedProperty'.".format(
                                schema.get("type")
                            )
                        )
            elif key == "required":
                required = value
            elif key == "name":
                title = value

        if is_collection:
            raise HydraCollectionException("Parsed parameter is a collection.")

        property_processor = PropertyProcessor(prop, title, required)
        hydra_prop = property_processor.generate()
        return hydra_prop
