from utils import parser_class_mapping
from os.path import isdir


class RefParser:
    def __init__(self, pointer) -> None:
        self.pointer = pointer

    def find_root(self):
        path_to_ref = self.pointer.split("/")
        if path_to_ref[0] == "#":
            return path_to_ref[::1]
        elif isdir(path_to_ref[0]):
            return "directory"
        else:
            return "url"

    def parse(self):
        root = self.find_root()
        hydra_class = {}
        hydra_collection = {}
        if root == "directory":
            pass
        elif root == "url":
            pass
        else:
            # components within the same file
            from processors.api_class_processor import APIClassProcessor

            component_type = root[2]
            if component_type == "schemas":
                hydra_entity = root[3]
                hydra_class = APIClassProcessor.hydra_classes.get(hydra_entity)
                hydra_collection = APIClassProcessor.hydra_collections.get(hydra_entity)

        return [hydra_class, hydra_collection]
