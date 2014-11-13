import unittest

from .. import midi

class VLQTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def check(self, n, b):
        self.assertEqual(midi.VLQ.numberToBytes(n), b, 'Wrong conversion Number->Bytes')

    def test_byte_length(self):
        self.assertEqual(len(midi.VLQ.numberToBytes(0)), 4, 'Byte length must be 4')
        self.assertEqual(len(midi.VLQ.numberToBytes(0xFFFFFFFF)), 4, 'Byte length must be 4')
        self.assertEqual(len(midi.VLQ.numberToBytes(0xFFFFFFFFFFFFFFFFFFF)), 4, 'Byte length must be 4')

    def test_conversion1(self):
        n = 1
        b = b'\x00\x00\x00\x01'
        self.check(n, b)

    def test_conversion400(self):
        n = 400
        b = b'\x00\x00\x83\x10'
        self.check(n, b)

    def test_conversion1800(self):
        n = 1800
        b = b'\x00\x00\x8e\x08'
        self.check(n, b)

    def test_conversion106903(self):
        n = 106903
        b = b'\x00\x86\xC3\x17'
        self.check(n, b)


if __name__ == '__main__':
    unittest.main()