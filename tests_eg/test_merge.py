from .context import logging_eg
from logging_eg import dictmerge
import unittest

class TestDictMerge(unittest.TestCase):

    def test_should_merge_simple_dicts(self):
        d1 = {"a": "a", "b": 2}
        d2 = {"c": 2, "d":3}
        expected = {"a": "a", "b": 2, "c": 2, "d":3}
        result = dictmerge.merge(d1,d2)
        self.assertEqual(expected, result)

    def test_should_merge_dicts_with_lists(self):
        d1 = {"a": "a", "b": [2]}
        d2 = {"c": 2, "d": [3]}
        expected = {"a": "a", "b": [2], "c": 2, "d": [3]}
        result = dictmerge.merge(d1,d2)
        self.assertEqual(expected, result)

    def test_should_merge_dicts_with_conficting_lists(self):
        d1 = {"a": "a", "b": [2]}
        d2 = {"c": 2, "b": [3]}
        expected = {"a": "a", "b": [3], "c": 2 }
        result = dictmerge.merge(d1,d2)
        self.assertEqual(expected, result)

    def test_should_merge_overlapping_dicts(self):
        d1 = {"a": "a", "b": 2}
        d2 = {"b": 4, "d":3}
        expected = {"a": "a", "b": 4, "d":3}
        result = dictmerge.merge(d1,d2)
        self.assertEqual(expected, result)


    def test_should_merge_nested_dicts(self):
        d1 = {"a": "a", "b": {"fred": "cool"}}
        d2 = {"b": {"fred": {"status": "notcool"}}, "d":3}
        expected = {"a": "a", "b": {"fred": {"status": "notcool"}}, "d":3}
        result = dictmerge.merge(d1,d2)
        self.assertEqual(expected, result)

    def test_should_merge_nested_dicts_with_lists(self):
        d1 = {"a": "a", "b": {"fred": {"status": ["cool"] } }}

        d2 = {"b": {"fred": {"status": ["notcool"]}}, "d":3}

        expected = {"a": "a", "b": {"fred": {"status": ["notcool"]}}, "d":3}
        result = dictmerge.merge(d1,d2)
        self.assertEqual(expected, result)