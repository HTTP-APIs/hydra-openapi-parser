from hydra_python_core.doc_writer import HydraClassProp, HydraLink
from typing import Union


class PropertyProcessor:
    def __init__(self, prop: Union[str, HydraLink], title: str, required: bool) -> None:
        self.prop = prop
        self.title = title
        self.required = required

    def generate(self):
        hydra_prop = HydraClassProp(
            prop=self.prop,
            title=self.title,
            read=False,
            write=False,
            required=self.required,
        )

        return hydra_prop
