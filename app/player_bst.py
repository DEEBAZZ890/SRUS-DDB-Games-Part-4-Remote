from typing import Optional

from app.player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self) -> None:
        self._root = Optional[PlayerBNode] = None

    @property
    def root(self) -> Optional[PlayerBNode]:
        return self._root

    @root.setter
    def root(self, value: Optional[PlayerBNode]) -> None:
        self._root = value
