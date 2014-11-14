import unittest
from .. import translate

class TranlatorTestCase(unittest.TestCase):

    def setUp(self):
        self.trans = translate.Translator()

    def test_events_k(self):
        text = 'k'
        evs = [
            (0, 1),
            (3, 0),
            (1, 1),
            (1, 0),
            (1, 1),
            (3, 0),
        ]
        events = self.trans.textToEvents(text)
        self.assertEqual(events, evs, 'K not tranlated well')
