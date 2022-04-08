from processors.status_processor import StatusProcessor
from parsers.schema_parser import SchemaParser


class ResponseParser:
    def __init__(self, code, response) -> None:
        self.code = code
        self.response = response
        self.returns = ""

    def parse_code(self):
        if self.code.isnumeric():
            return int(self.code)
        else:
            # handles default response
            return 500

    def parse_returns(self):
        return self.returns

    def parse(self):
        response = {"code": self.parse_code(), "desc": "", "title": ""}
        for key, value in self.response.items():
            if key == "description":
                response["desc"] = value
            if key == "content":
                for _, expects in value.items():
                    schema_parser = SchemaParser(expects.get("schema"))
                    hydra_classes, _ = schema_parser.parse()
                    for title, _ in hydra_classes.items():
                        self.returns = title

        status_processor = StatusProcessor(response)
        hydra_status = status_processor.generate()

        return hydra_status
