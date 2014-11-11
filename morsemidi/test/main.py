import unittest
import morse

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(morse)
    runner = unittest.TextTestRunner()
    runner.runsuite
