from typing import Union, List, Dict
from hydra_python_core.doc_writer import (
    HydraClassOp,
    HydraClassProp,
)
from exceptions import HydraCollectionException
from parsers.method_parser import MethodParser


class PathParser:
    def __init__(self, path_name, path_method, id) -> None:
        self.path_method = path_method
        self.id = f'{id}?resource={path_name.split("/")[1].capitalize()}'
        self.hydra_class_ops = []
        self.hydra_class_props = []
        self.hydra_collection_ops = {}

    def is_parsed(self):
        if self.hydra_class_ops or self.hydra_collection_ops or self.hydra_class_props:
            return True
        return False

    def get_class_props(self):
        if not self.is_parsed():
            self.parse()
        return self.hydra_class_props

    def get_class_ops(self) -> List[HydraClassOp]:
        if not self.is_parsed():
            self.parse()
        return self.hydra_class_ops

    def get_collection_ops(self) -> Dict[str, bool]:
        if not self.is_parsed():
            self.parse()
        return self.hydra_collection_ops

    def parse(self) -> None:
        for method_name, method_details in self.path_method.items():
            try:
                method_parser = MethodParser(method_name, method_details, self.id)
                hydra_class_op_, hydra_class_props_ = method_parser.parse()
                self.hydra_class_ops.append(hydra_class_op_)
                self.hydra_class_props.extend(hydra_class_props_)
            except HydraCollectionException:
                self.hydra_collection_ops[method_name] = True
