import unittest

from morsemidi.test import morse, midi

if __name__ == '__main__':
    modules = [morse, midi]

    suite = unittest.TestSuite()
    for module in modules:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(module))
    unittest.TextTestRunner().run(suite)