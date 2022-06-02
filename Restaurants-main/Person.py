from abc import ABC

class Person(ABC):
    def __init__(
            self,
            name: str,
            id: int     
    ) -> None:
        self.name = name
        self.id = id
        