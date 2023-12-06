from __future__ import annotations
from typing import Optional
from app.player import Player


class PlayerBNode:
    def __init__(self, player: Player) -> None:
        self._player = player
        self._left: Optional[PlayerBNode] = None
        self._right: Optional[PlayerBNode] = None

    @property
    def player(self) -> Player:
        return self._player

    @player.setter
    def player(self, value: Player) -> None:
        self._player = value

    @property
    def left(self) -> Optional[PlayerBNode]:
        return self._left

    @left.setter
    def left(self, node: Optional[PlayerBNode]) -> None:
        self._left = node

    @property
    def right(self) -> Optional[PlayerBNode]:
        return self._right

    @right.setter
    def right(self, node: Optional[PlayerBNode]) -> None:
        self._right = node


