import os
import yaml
from processors.api_info_processor import APIInfoProcessor
from processors.api_class_processor import APIClassProcessor
from utils import gen_entrypoint, gen_doc_file
from hydra_python_core.doc_writer import HydraStatus


class OpenAPIDocParser:
    def __init__(self, inp_path: str) -> None:
        # construct the path for the input OpenAPI doc
        self.current_dir = os.path.dirname(__file__)
        input_file_path = os.path.join(self.current_dir, inp_path)
        with open(input_file_path) as stream:
            try:
                self.openapi_doc = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def parse(self, out_path: str) -> str:
        # create basic hydra doc with general info (@id, @context, description etc.)
        info = APIInfoProcessor(self.openapi_doc)
        api_info_doc = info.generate()
        api_doc = gen_entrypoint(api_info_doc)

        # create supported classes for hydra doc
        api_classes = APIClassProcessor(self.openapi_doc)
        supported_classes, supported_collections = api_classes.generate()
        for supported_class in supported_classes:
            api_doc.add_supported_class(supported_class)

        # create supported collections for hydra doc
        for supported_collection in supported_collections:
            api_doc.add_supported_collection(supported_collection)

        hydra_doc = api_doc.generate()

        if out_path:
            # construct the path for the output Hydra doc
            output_file_path = os.path.join(self.current_dir, out_path)
            with open(output_file_path, "w") as f:
                f.write(gen_doc_file(hydra_doc))

        return hydra_doc


if __name__ == "__main__":
    petstore_doc_path = "../../samples/v2/petstore-expanded.yaml"
    uspto_doc_path = "../../samples/v2/uspto.yaml"
    openapi_doc = OpenAPIDocParser(petstore_doc_path)
    hydra_doc = openapi_doc.parse("../../samples/v2/hydra_doc_sample.py")
