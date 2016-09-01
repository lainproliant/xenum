import unittest
from xenum import *

#--------------------------------------------------------------------
class XenumTests(unittest.TestCase):
    def test_enum_create(self):
        @xenum
        class Colors:
            RED = 1
            BLUE = 2
            GREEN = 3

        self.assertIsInstance(Colors.RED, Xenum)
        self.assertIsInstance(Colors.GREEN, Xenum)
        self.assertIsInstance(Colors.BLUE, Xenum)

    def test_assert_serialize(self):
        @xenum
        class Colors:
            RED = 1
            BLUE = 2
            GREEN = 3

        self.assertEqual(str(Colors.RED), "Colors.RED")
        self.assertEqual(str(Colors.GREEN), "Colors.GREEN")
        self.assertEqual(str(Colors.BLUE), "Colors.BLUE")

    def test_assert_deserialize(self):
        @xenum
        class Colors:
            RED = 1
            BLUE = 2
            GREEN = 3
    
        self.assertEqual(Colors.by_name("Colors.RED"), Colors.RED)
        self.assertEqual(Colors.by_name("Colors.GREEN"), Colors.GREEN)
        self.assertEqual(Colors.by_name("Colors.BLUE"), Colors.BLUE)

#--------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
