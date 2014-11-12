import unittest

from .. import midi

class VLQTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def check(self, n, b):
        self.assertEqual(midi.VLQ.numberToBytes(0), b, 'Wrong conversion Number->Bytes')
        self.assertEqual(midi.VLQ.bytesToNumber(b), n, 'Wrong conversion Bytes->Number')


    def test_conversion1(self):
        n = 0
        b = b'\x00\x00\x00\x01'
        self.check(n, b)


if __name__ == '__main__':
    unittest.main()