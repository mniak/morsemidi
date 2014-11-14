import unittest

from morsemidi.test import morse, midi, translate

if __name__ == '__main__':
    modules = [morse, midi, translate]

    suite = unittest.TestSuite()
    for module in modules:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(module))
    unittest.TextTestRunner().run(suite)