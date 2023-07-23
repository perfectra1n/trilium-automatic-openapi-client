from enum import Enum


class CreateRevisionFormat(str, Enum):
    HTML = "html"
    MARKDOWN = "markdown"

    def __str__(self) -> str:
        return str(self.value)
