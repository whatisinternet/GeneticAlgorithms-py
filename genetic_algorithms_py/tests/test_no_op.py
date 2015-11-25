from unittest import TestCase

import genetic_algorithms_py

class TestNoOp(TestCase):
    def test_is_string(self):
        s= genetic_algorithms_py.no_op()
        self.assertTrue(isinstance(s, basestring))
