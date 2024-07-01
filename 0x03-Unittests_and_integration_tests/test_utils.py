#!/usr/bin/env python3
"""
Test module for utils module
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b',), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        test that the method `access_nested_map` returns what it is
        supposed to
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',)),
        ({'a': 1}, ('a', 'b',)),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        test that the method `access_nested_map` raises a KeyError exception
        with invalid input
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
