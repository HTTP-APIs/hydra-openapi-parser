from hydra_python_core.doc_writer import (
    HydraClassOp,
    HydraClassProp,
    HydraError,
    HydraStatus,
)
from exceptions import HydraCollectionException
from processors.api_info_processor import APIInfoProcessor
from parsers.param_parser import ParameterParser
from parsers.resp_parser import ResponseParser
from processors.op_processor import OperationProcessor
from parsers.schema_parser import SchemaParser

from typing import Any, List, Dict, Union


class MethodParser:
    def __init__(self, method: str, method_details: Dict[str, Any], id: str) -> None:
        self.method = method.upper()
        self.method_details = method_details
        self.id = id

    def parse(self) -> List[Union[HydraClassOp, List[HydraClassProp]]]:
        method_title = str
        hydra_props: List[HydraClassProp] = []
        hydra_op: HydraClassOp
        possible_status: List[Union[HydraStatus, HydraError]] = []
        expects_resource = ""
        returns_resource = ""
        for key, value in self.method_details.items():
            if key == "parameters":
                for parameter in value:
                    param_parser = ParameterParser(parameter)
                    hydra_class_prop = param_parser.parse()
                    hydra_props.append(hydra_class_prop)
            elif key == "responses":
                for code, response in value.items():
                    response_parser = ResponseParser(code, response)
                    hydra_status = response_parser.parse()
                    possible_status.append(hydra_status)
                    if response_parser.parse_code() != 500:
                        returns_resource = response_parser.parse_returns()

            elif key == "operationId":
                method_title = value
            elif key == "requestBody":
                request_content = value.get("content")
                for _, expects in request_content.items():
                    schema_parser = SchemaParser(expects.get("schema"))
                    hydra_classes, _ = schema_parser.parse()
                    for title, _ in hydra_classes.items():
                        expects_resource = title

        operation_processor = OperationProcessor(
            title=method_title,
            method=self.method,
            id=self.id,
            possible_status=possible_status,
            expects=expects_resource,
            returns=returns_resource,
        )
        hydra_op = operation_processor.generate()

        return [hydra_op, hydra_props]
