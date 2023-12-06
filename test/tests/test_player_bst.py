import unittest
from app.player import Player
from app.player_bst import PlayerBST


class TestPlayerBSTClass(unittest.TestCase):

    def setUp(self) -> None:
        self.players = [
            Player("10472204", "John"),
            Player("29543305", "Brayden"),
            Player("10983546", "Sarah"),
            Player("12345678", "Michaela"),
            Player("11111111", "Alex")
        ]
        for i, score in enumerate([30, 20, 25, 15, 30]):
            self.players[i].score = score
        self.bst = PlayerBST()
        for player in self.players:
            self.bst.insert(player)

    def test_insert_functionality(self):
        new_player = Player("20069321", "NewPlayer")
        self.bst.insert(new_player)
        found_player = self.bst.search("NewPlayer")
        self.assertIsNotNone(found_player)
        self.assertEqual(found_player.name, "NewPlayer")

    def test_search_functionality(self):
        found_player = self.bst.search("John")
        self.assertIsNotNone(found_player)
        self.assertEqual(found_player.name, "John")

    def test_handle_duplicates(self):
        duplicate_player = Player("new_uid", "John")
        self.bst.insert(duplicate_player)
        found_player = self.bst.search("John")
        self.assertIsNotNone(found_player)
        self.assertEqual(found_player.uid, "new_uid")

    def test_in_order_traversal(self):
        bst_sorted_list = self.bst.to_list()
        sorted_names = sorted([player.name for player in self.players])
        self.assertEqual([player.name for player in bst_sorted_list], sorted_names)

    def test_smaller_number_at_left_node(self):
        self.assertIsNotNone(self.bst.root.left)
        self.assertLess(self.bst.root.left.player.name, self.bst.root.player.name)

    def test_greater_number_at_right_node(self):
        self.assertIsNotNone(self.bst.root.right)
        self.assertGreater(self.bst.root.right.player.name, self.bst.root.player.name)

    def test_bst_insert_rules(self):
        self.check_structure(self.bst.root, "John", "Brayden", "Sarah")

    def check_structure(self, node, expected_root, expected_left, expected_right):
        self.assertIsNotNone(node)
        self.assertEqual(node.player.name, expected_root)
        if expected_left is not None:
            self.assertIsNotNone(node.left)
            self.assertLess(node.left.player.name, node.player.name)
        if expected_right is not None:
            self.assertIsNotNone(node.right)
            self.assertGreater(node.right.player.name, node.player.name)

