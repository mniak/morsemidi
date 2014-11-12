import unittest

from .. import morse

class Morse(unittest.TestCase):

    def setUp(self):
        self.morse = morse.Morse()

    def test_translate_text(self):
        text = self.morse.translate('the quick brown fox jumps over the lazy dog')
        morse = '-,....,.;--.-,..-,..,-.-.,-.-;-...,.-.,---,.--,-.;..-.,---,-..-;.---,..-,--,.--.,...;---,...-,.,.-.;-,....,.;.-..,.-,--..,-.--;-..,---,--.'
        self.assertEquals(text, morse, 'Morse translation not working')

    def test_translate_abcde(self):
        text = 'abcde'
        morse1 = self.morse.translate('abcde')
        morse2 = '.-,-...,-.-.,-..,.'
        self.assertEquals(morse1, morse2, 'Morse translation not working: "' + text + '"')

    def test_translate_fghij(self):
        text = 'fghij'
        morse1 = self.morse.translate(text)
        morse2 = '..-.,--.,....,..,.---'
        self.assertEquals(morse1, morse2, 'Morse translation not working: "' + text + '"')

    def test_translate_klmno(self):
        text = 'klmno'
        morse1 = self.morse.translate(text)
        morse2 = '-.-,.-..,--,-.,---'
        self.assertEquals(morse1, morse2, 'Morse translation not working: "' + text + '"')

    def test_translate_pqrst(self):
        text = 'pqrst'
        morse1 = self.morse.translate(text)
        morse2 = '.--.,--.-,.-.,...,-'
        self.assertEquals(morse1, morse2, 'Morse translation not working: "' + text + '"')

    def test_translate_uvwxyz(self):
        text = 'uvwxyz'
        morse1 = self.morse.translate(text)
        morse2 = '..-,...-,.--,-..-,-.--,--..'
        self.assertEquals(morse1, morse2, 'Morse translation not working: "' + text + '"')

    def test_translate_spaces(self):
        text = 'k m'
        morse1 = self.morse.translate(text)
        morse2 = '-.-;--'
        self.assertEquals(morse1, morse2, 'Morse spaces translation')

    def test_translate_char(self):
        morse1 = self.morse.translate('a')
        morse2 = '.-'
        self.assertEquals(morse1, morse2, 'Morse char translation "a"')

