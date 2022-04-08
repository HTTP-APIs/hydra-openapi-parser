from typing import Dict, Optional, Union
from hydra_python_core.doc_writer import HydraCollection, HydraLink


class CollectionProcessor:
    def __init__(
        self,
        title: str,
        id: Union[str, HydraLink],
        desc: str = "",
        hydra_ops: Dict[str, bool] = {},
        manages: Optional[Dict[str, str]] = {},
    ) -> None:
        self.title = title + "Collection"
        self.desc = desc if desc else f"A collection for {title.lower()}"
        self.hydra_ops = hydra_ops
        self.manages = (
            manages
            if manages
            else {"object": f"{id}?resource={title}", "property": "rdfs:type"}
        )

    def generate(self) -> HydraCollection:
        hydra_collection = HydraCollection(
            collection_name=self.title,
            collection_description=self.desc,
            manages=self.manages,
            get=self.hydra_ops.get("get", False),
            put=self.hydra_ops.get("put", False),
            post=self.hydra_ops.get("post", False),
            delete=self.hydra_ops.get("delete", False),
        )
        return hydra_collection
