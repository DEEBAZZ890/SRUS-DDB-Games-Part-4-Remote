from app.player import Player
from app.player_node import PlayerNode
from typing import List, Optional


class PlayerList:
    def __init__(self) -> None:
        self._head: Optional[PlayerNode] = None
        self._tail: Optional[PlayerNode] = None

    @property
    def head(self) -> Optional[PlayerNode]:
        return self._head

    @property
    def tail(self) -> Optional[PlayerNode]:
        return self._tail

    @tail.setter
    def tail(self, new_node: Optional[PlayerNode]) -> None:
        self._tail = new_node

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f'{class_name}(Player Nodes={self.to_list()})'

    def is_empty(self) -> bool:
        """If no head is present, the list is empty"""
        return self._head is None

    def to_list(self) -> List[str]:
        """Returns a string repr of the linked list for each player"""
        my_list: List[str] = []
        current_player = self._head
        while current_player:
            my_list.append(repr(current_player))
            current_player = current_player.next_player
        return my_list

    def display(self, forward=True) -> None:
        """Prints to standard out, the contents of the linked list in a specified order"""
        if self.is_empty():
            raise ValueError("List is empty")
        if forward:
            current = self._head
            while current is not None:
                print(current)
                current = current.next_player
        else:
            current = self._tail
            while current is not None:
                print(current)
                current = current.previous_player

    def insert_head_node(self, player: Player) -> None:
        """Designates new player as new head node. If the list is empty, is designated as head and tail"""
        new_player = PlayerNode(player)
        if self.is_empty():
            self._head = new_player
            self._tail = new_player
        else:
            new_player.next_player = self._head
            if self._head is not None:  # added to address mypy error
                self._head.previous_player = new_player
            self._head = new_player

    def insert_tail_node(self, player: Player) -> None:
        """Assigns given player as new tail node. If list is empty, New player is designated as head and tail"""
        new_player = PlayerNode(player)
        if self.is_empty():
            self._head = new_player
            self._tail = new_player
        else:
            new_player.previous_player = self._tail
            if self._tail is not None:  # added to address mypy error
                self._tail.next_player = new_player
            self._tail = new_player

    def delete_head_node(self) -> None:
        """Elects new head node using head.next_player attribute. If no head node exists, raises value error."""
        if self.is_empty():
            raise ValueError("Deletion failed. List is empty; No head node exists")

        if self._head:  # added to address mypy error
            existing_head = self._head
            self._head = existing_head.next_player

            if self._head is None:
                self._tail = None
            else:
                self._head.previous_player = None

    def delete_node_by_key_excluding_ends(self, key: str) -> None:
        """Searches from the second node to the tail and deletes the matching player by key."""
        player_node = self._head.next_player if self._head else None

        while player_node is not None:
            if player_node.key == key:  # added to address mypy error
                if player_node.previous_player is not None:
                    player_node.previous_player.next_player = player_node.next_player
                if player_node.next_player is not None:
                    player_node.next_player.previous_player = player_node.previous_player
                return
            player_node = player_node.next_player
        raise ValueError(f"Player with UID: {key} not found. Deletion Failed")

    def delete_tail_node(self) -> None:
        """
           If tail doesn't exist, raises value error. Otherwise, elects previous player attribute of existing tail
           as the new tail node
        """
        if self._tail is None:
            raise ValueError("Deletion failed. List is empty; No tail node exists")

        existing_tail = self._tail
        self._tail = existing_tail.previous_player

        if self._tail is None:
            self._head = None
        else:
            self._tail.next_player = None

    def delete_player_node_by_key(self, key: str) -> None:
        """
           Deletes a player node from the list based on the given key (uid).
           Handles deletion of head, tail, and nodes in between.
        """
        if self.is_empty():
            raise ValueError(f"List is empty. Cannot delete player with key {key}.")

        if self._head and self._head.key == key:
            self.delete_head_node()
            return

        if self._tail and self._tail.key == key:
            self.delete_tail_node()
            return

        self.delete_node_by_key_excluding_ends(key)

