from enum import Enum


class AttributeType(str, Enum):
    LABEL = "label"
    RELATION = "relation"

    def __str__(self) -> str:
        return str(self.value)
