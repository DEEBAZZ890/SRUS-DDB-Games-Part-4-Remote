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
        """Test that a new player can be inserted into the BST. Validate insert success using search method."""
        new_player = Player("20069321", "NewPlayer")
        self.bst.insert(new_player)
        found_player = self.bst.search("NewPlayer")
        self.assertIsNotNone(found_player)
        self.assertEqual(found_player.name, "NewPlayer")

    def test_search_functionality(self):
        """Tests the search method by ensuring it correctly finds an existing player by name from the pre-build BST."""
        found_player = self.bst.search("John")
        self.assertIsNotNone(found_player)
        self.assertEqual(found_player.name, "John")

    def test_duplicate_handling_update_attribute(self):
        """Verify that inserting a player with the same key will update the existing nodes score"""
        player_to_update = self.bst.search("John")
        player_to_update.score = 30
        self.bst.insert(player_to_update)

        found_player = self.bst.search("John")
        self.assertIsNotNone(found_player)
        self.assertEqual(found_player.score, 30)

    def test_duplicate_handling_same_key(self):
        """Verify that inserting a player with the same key will update the existing nodes uid"""
        duplicate_player = Player("new_uid", "John")
        duplicate_player.score = 20
        self.bst.insert(duplicate_player)

        found_player = self.bst.search("John")
        self.assertIsNotNone(found_player)
        self.assertEqual(found_player.uid, "new_uid")

    def test_in_order_traversal(self):
        """Verify that the in-order traversal method correctly returns players sorted by key (name)."""
        bst_sorted_list = self.bst.to_list()
        sorted_names = sorted([player.name for player in self.players])
        self.assertEqual([player.name for player in bst_sorted_list], sorted_names)

    def test_smaller_number_at_left_node(self):
        """Confirms that the left child node in the BST has a key smaller than its parent node."""
        self.assertIsNotNone(self.bst.root.left)
        self.assertLess(self.bst.root.left.player.name, self.bst.root.player.name)

    def test_greater_number_at_right_node(self):
        """Ensures that the right child node in the BST has a key greater than its parent node."""
        self.assertIsNotNone(self.bst.root.right)
        self.assertGreater(self.bst.root.right.player.name, self.bst.root.player.name)

    def test_bst_insert_rules(self):
        self.valid_bst_structure(self.bst.root, "John", "Brayden", "Sarah")

    def valid_bst_structure(self, node, expected_root, expected_left, expected_right):
        """
           Helper method for the test_bst_insert_rules method which \n
           validates that inserted nodes adhere to BST properties: \n
           - Ensures the left child node (if present) is less than the root node/parent node.
           - Ensures the right child node (if present) is greater than the root node/parent node.
        """
        self.assertIsNotNone(node)
        self.assertEqual(node.player.name, expected_root)
        if expected_left is not None:
            self.assertIsNotNone(node.left)
            self.assertLess(node.left.player.name, node.player.name)
        if expected_right is not None:
            self.assertIsNotNone(node.right)
            self.assertGreater(node.right.player.name, node.player.name)

    def test_empty_tree_in_order_traversal(self):
        """Checks that in-order traversal on an empty BST returns an empty list."""
        empty_bst = PlayerBST()
        self.assertEqual(empty_bst.to_list(), [])

    def test_empty_tree_search(self):
        """Validate that searching in an empty BST returns None, indicating no player found."""
        empty_bst = PlayerBST()
        self.assertIsNone(empty_bst.search("Nonexistent"))

    def test_empty_tree_balance(self):
        """Verifies that balancing an empty BST keeps it empty, ensuring method handles empty tree correctly."""
        empty_bst = PlayerBST()
        empty_bst.balance_bst()
        self.assertTrue(empty_bst.is_empty())


