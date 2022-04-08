from hydra_python_core.doc_writer import (
    HydraClass,
    HydraClassOp,
    HydraClassProp,
    HydraLink,
)
from typing import List, Union, Optional


class ClassProcessor:
    def __init__(
        self,
        title: str,
        id: Union[str, HydraLink],
        desc: str = "",
        hydra_ops: List[HydraClassOp] = [],
        hydra_props: List[HydraClassProp] = [],
    ) -> None:
        self.title = title
        self.desc = desc if desc else f"Class for {title}"
        self.hydra_ops = hydra_ops
        self.hydra_props = self.filter_props(hydra_props)
        self.id = id

    @staticmethod
    def filter_props(objects):
        filtered_objs = {}
        for object_ in objects:
            title = object_.__dict__.get("title")
            if not filtered_objs.get(title):
                filtered_objs[title] = object_
            elif object_.__dict__ != filtered_objs.get(title).__dict__:
                filtered_objs[title] = object_
        return filtered_objs.values()

    def generate(self) -> HydraClass:
        hydra_class = HydraClass(
            title=self.title,
            desc=self.desc,
            _id=self.id,
            endpoint=True,
        )

        for hydra_op in self.hydra_ops:
            hydra_class.add_supported_op(hydra_op)

        for hydra_prop in self.hydra_props:
            hydra_class.add_supported_prop(hydra_prop)

        return hydra_class
