from hydra_python_core.doc_writer import HydraStatus


class StatusProcessor:
    def __init__(self, response) -> None:
        self.response = response

    def generate(self):
        hydra_status = HydraStatus(
            code=self.response["code"],
            title=self.response["title"],
            desc=self.response["desc"],
        )

        return hydra_status
