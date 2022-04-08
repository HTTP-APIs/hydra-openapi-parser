from hydra_python_core.doc_writer import HydraClassOp, HydraStatus, HydraError
from typing import List, Union


class OperationProcessor:
    def __init__(
        self,
        title: str,
        method: str,
        id: str,
        expects: str = None,
        returns: str = None,
        expects_header: List[str] = [],
        returns_header: List[str] = [],
        possible_status: List[Union[HydraStatus, HydraError]] = [],
    ) -> None:
        self.method = method.upper()
        self.title = title
        self.expects = expects
        self.returns = returns
        self.expects_header = expects_header
        self.returns_header = returns_header
        self.possible_status = possible_status
        if returns:
            self.returns = id.replace(f"?resource={title}", f"?resource={returns}")
        if expects:
            self.expects = id.replace(f"?resource={title}", f"?resource={expects}")

    def generate(self):
        hydra_class_op = HydraClassOp(
            title=self.title,
            method=self.method,
            expects=self.expects,
            returns=self.returns,
            expects_header=self.expects_header,
            returns_header=self.returns_header,
            possible_status=self.possible_status,
        )
        return hydra_class_op
