from unittest import TestCase

from coolname_hash import pseudohash_slug_v1 as pseudohash_slug


class TestCoolname(TestCase):

    def test_pseudohash_slug(self):
        self.assertEqual(pseudohash_slug(123), 'hissing-sage-buzzard-of-faith')
        self.assertEqual(pseudohash_slug(456), 'strict-aloof-dolphin-of-purring')
        self.assertRaises(ValueError, pseudohash_slug, [123])


    def test_pseudohash_slug_int_equal_str(self):
        # int = str = bytes, if it's the same number
        self.assertEqual(pseudohash_slug('123'), pseudohash_slug(123))
        self.assertEqual(pseudohash_slug('123'), pseudohash_slug(b'123'))
