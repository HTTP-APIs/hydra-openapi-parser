class HydraCollectionException(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


class ExpectsValueError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
