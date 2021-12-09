from utils import component_class_mapping


class ComponentParser:
    def __init__(self, component, definition) -> None:
        self.component = component
        self.definition = definition

    def parse(self):
        Parser = component_class_mapping(self.component)
        parser = Parser(self.definition)
        return parser.parse()
