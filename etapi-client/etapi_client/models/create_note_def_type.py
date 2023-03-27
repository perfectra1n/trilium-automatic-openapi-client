from enum import Enum


class CreateNoteDefType(str, Enum):
    BOOK = "book"
    CODE = "code"
    FILE = "file"
    IMAGE = "image"
    RELATIONMAP = "relationMap"
    RENDER = "render"
    SEARCH = "search"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
