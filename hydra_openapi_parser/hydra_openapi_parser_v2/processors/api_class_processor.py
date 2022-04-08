from parsers.ref_parser import RefParser
from processors.api_info_processor import APIInfoProcessor
from processors.class_processor import ClassProcessor
from processors.collection_processor import CollectionProcessor
from parsers.components_parser import ComponentParser
from parsers.path_parser import PathParser
from hydra_python_core.doc_writer import HydraClass, HydraCollection
from typing import Dict, List, Any, Union


class APIClassProcessor:
    hydra_classes: Dict[str, HydraClass] = {}
    hydra_collections: Dict[str, HydraCollection] = {}

    def __init__(self, openapi_doc: Dict[str, Any]) -> None:
        self.doc = openapi_doc
        self.id = APIInfoProcessor.api_info["id"]

    def generate_from_components(self):
        for component, definition in self.doc.get("components").items():
            component_parser = ComponentParser(component, definition)
            component_classes, component_collections = component_parser.parse()
            return [component_classes, component_collections]

    def generate_from_paths(self):
        hydra_title = str
        hydra_classes = {}
        hydra_collections = {}

        for path_name, path_method in self.doc.get("paths").items():
            hydra_title = path_name.split("/")[1].capitalize()
            if path_method.get("$ref"):
                ref_parser = RefParser(path_method.get("$ref"))
                hydra_class, hydra_collection = ref_parser.parse()
                APIClassProcessor.hydra_classes[hydra_title] = hydra_class
                APIClassProcessor.hydra_collections[hydra_title] = hydra_collection
            else:
                path_parser = PathParser(path_name, path_method, self.id)
                hydra_class_ops = path_parser.get_class_ops()
                hydra_class_props = path_parser.get_class_props()
                hydra_collection_ops = path_parser.get_collection_ops()
                if not hydra_classes.get(hydra_title):
                    hydra_classes[hydra_title] = [[], []]
                if not hydra_collections.get(hydra_title):
                    hydra_collections[hydra_title] = {}
                hydra_classes[hydra_title][0].extend(hydra_class_ops)
                hydra_classes[hydra_title][1].extend(hydra_class_props)
                hydra_collections[hydra_title].update(hydra_collection_ops)

        return [hydra_classes, hydra_collections]

    def generate(self) -> List[List[Union[HydraClass, HydraCollection]]]:
        component_classes, component_collections = self.generate_from_components()
        APIClassProcessor.hydra_classes.update(component_classes)
        APIClassProcessor.hydra_collections.update(component_collections)

        path_classes, path_collections = self.generate_from_paths()
        for hydra_title, [hydra_ops, hydra_props] in path_classes.items():
            class_processor = ClassProcessor(
                title=hydra_title,
                id=self.id,
                hydra_ops=hydra_ops,
                hydra_props=hydra_props,
            )
            hydra_class = class_processor.generate()
            APIClassProcessor.hydra_classes[hydra_title] = hydra_class

        for hydra_title, hydra_ops in path_collections.items():
            collection_processor = CollectionProcessor(
                title=hydra_title, id=self.id, hydra_ops=hydra_ops
            )
            hydra_collection = collection_processor.generate()
            APIClassProcessor.hydra_collections[hydra_title] = hydra_collection

        hydra_classes_ = list(APIClassProcessor.hydra_classes.values())
        hydra_collections_ = list(APIClassProcessor.hydra_collections.values())
        return [hydra_classes_, hydra_collections_]
