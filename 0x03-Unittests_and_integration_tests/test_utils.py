#!/usr/bin/env python3
"""
Test module for utils module
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import (
        access_nested_map,
        get_json,
        memoize,
)


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


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        test that the method `get_json` returns the expected result
        """
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        """
        test the `utils.memoize` decorator
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method', return_value=42) \
                as mock_a_method:
            myobj = TestClass()
            self.assertEqual(myobj.a_property, 42)  # first call
            self.assertEqual(myobj.a_property, 42)  # second call
            mock_a_method.assert_called_once()
