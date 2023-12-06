from typing import Optional, List
from app.player import Player
from app.player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self) -> None:
        self._root: Optional[PlayerBNode] = None

    @property
    def root(self) -> Optional[PlayerBNode]:
        return self._root

    @root.setter
    def root(self, value: Optional[PlayerBNode]) -> None:
        self._root = value

    def is_empty(self) -> bool:
        return self._root is None

    def to_list(self) -> List[Player]:
        return list(self._in_order_traversal(self._root))

    def _in_order_traversal(self, node: Optional[PlayerBNode]):
        """Adopted from raf's notes in week 9. Uses yield to retrieve respective node values when traversing the tree"""
        if node is not None:
            yield from self._in_order_traversal(node.left)
            yield node.player
            yield from self._in_order_traversal(node.right)

    def insert(self, player: Player) -> None:
        """Player is inserted at root node if root is empty. Otherwise, recursive insert is called to add new node"""
        if self.root is None:
            self.root = PlayerBNode(player)
        else:
            self._insert_recursive(self.root, player)

    def _insert_recursive(self, node: PlayerBNode, player: Player) -> None:
        """Logic for the insertion. Executes if root is not empty"""
        if player.name < node.player.name:
            if node.left is None:
                node.left = PlayerBNode(player)
            else:
                self._insert_recursive(node.left, player)
        elif player.name > node.player.name:
            if node.right is None:
                node.right = PlayerBNode(player)
            else:
                self._insert_recursive(node.right, player)
        else:
            node.player = player

    def search(self, name: str) -> Optional[Player]:
        return self._search_recursive(self._root, name)

    def _search_recursive(self, node: Optional[PlayerBNode], name: str) -> Optional[Player]:
        if node is None or node.player.name == name:
            return node.player if node else None
        elif name < node.player.name:
            return self._search_recursive(node.left, name)
        else:
            return self._search_recursive(node.right, name)

    def balance_bst(self) -> None:
        players = self.to_list()
        self._root = self._balance_bst_recursive(players)

    def _balance_bst_recursive(self, players: List[Player]) -> Optional[PlayerBNode]:
        if not players:
            return None
        mid = len(players) // 2
        node = PlayerBNode(players[mid])
        node.left = self._balance_bst_recursive(players[:mid])
        node.right = self._balance_bst_recursive(players[mid + 1:])
        return node
