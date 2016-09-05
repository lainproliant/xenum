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

    def test_ordered_values(self):
        @xenum
        class Alphabet:
            A = 'a'
            B = 'b'
            C = 'c'
            D = 'd'
            E = 'e'
            F = 'f'
            G = 'g'
            H = 'h'
            I = 'i'
            J = 'j'
            K = 'k'
            L = 'l'
            M = 'm'
            N = 'n'
            O = 'o'
            P = 'p'
            Q = 'q'
            R = 'r'
            S = 's'
            T = 't'
            U = 'u'
            V = 'v'
            W = 'w'
            X = 'x'
            Y = 'y'
            Z = 'z'

        self.assertEqual(list(Alphabet.values()), [
            Alphabet.A,
            Alphabet.B,
            Alphabet.C,
            Alphabet.D,
            Alphabet.E,
            Alphabet.F,
            Alphabet.G,
            Alphabet.H,
            Alphabet.I,
            Alphabet.J,
            Alphabet.K,
            Alphabet.L,
            Alphabet.M,
            Alphabet.N,
            Alphabet.O,
            Alphabet.P,
            Alphabet.Q,
            Alphabet.R,
            Alphabet.S,
            Alphabet.T,
            Alphabet.U,
            Alphabet.V,
            Alphabet.W,
            Alphabet.X,
            Alphabet.Y,
            Alphabet.Z])

    def test_selftyped_enum(self):
        @xenum
        class Action:
            INSERT = ctor('insert')
            UPDATE = ctor('update')
            DELETE = ctor('delete')

            def __init__(self, name):
                self.name = name

        self.assertIsInstance(Action.INSERT.value, Action)
        self.assertIsInstance(Action.UPDATE.value, Action)
        self.assertIsInstance(Action.DELETE.value, Action)

        self.assertEqual(Action.INSERT.value.name, 'insert')
        self.assertEqual(Action.UPDATE.value.name, 'update')
        self.assertEqual(Action.DELETE.value.name, 'delete')

#--------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
