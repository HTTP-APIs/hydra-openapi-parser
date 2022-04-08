from typing import Any, Dict
from parsers.api_info_parser import InfoParser
from hydra_python_core.doc_writer import HydraDoc


class APIInfoProcessor:
    api_info: Dict[str, str] = {}

    def __init__(self, openapi_doc: Dict[str, Any]) -> None:
        self.doc = openapi_doc

    def generate(self) -> HydraDoc:
        info_parser = InfoParser(self.doc)
        APIInfoProcessor.api_info = info_parser.parse()

        api_info_doc = HydraDoc(
            API=APIInfoProcessor.api_info["api"],
            title=APIInfoProcessor.api_info["title"],
            desc=APIInfoProcessor.api_info["desc"],
            entrypoint=APIInfoProcessor.api_info["entrypoint"],
            base_url=APIInfoProcessor.api_info["base_url"],
            doc_name=APIInfoProcessor.api_info["doc_name"],
        )
        return api_info_doc
