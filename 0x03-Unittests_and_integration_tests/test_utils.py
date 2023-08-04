#!/usr/bin/env python3
"""Test Utils models
"""
import unittest
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test Suit for access_nested_map
    """
    @parameterized.expand([
       ("negative", {"a": 1}, ("a",), 1),
       ("integer", {"a": {"b": 2}}, ("a",), {"b": 2}),
       ("large fraction", {"a": {"b": 2}}, ("a", "b"), 2),
   ])
    def test_access_nested_map(self, _, nested_map, path, expected):
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
