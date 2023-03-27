from enum import Enum


class NoteType(str, Enum):
    BOOK = "book"
    CODE = "code"
    FILE = "file"
    IMAGE = "image"
    MERMAID = "mermaid"
    NOTEMAP = "noteMap"
    RELATIONMAP = "relationMap"
    RENDER = "render"
    SEARCH = "search"
    SHORTCUT = "shortcut"
    TEXT = "text"
    WEBVIEW = "webView"

    def __str__(self) -> str:
        return str(self.value)
