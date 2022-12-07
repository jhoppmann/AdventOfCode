from __future__ import annotations
from typing import Union


class Dir:
    def __init__(self, name: str, parent: Dir):
        self.parent = parent
        self.children = {}
        self.name = name

    def add_child(self, child: Union[File, Dir]):
        self.children[child.name] = child


class File:
    def __init__(self, name: str, size: int, parent: Dir):
        self.name = name
        self.size = size
        self.parent = parent
