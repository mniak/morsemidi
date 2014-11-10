class Morse():
    def __init__(self):
        self.table = {
            'a': '.-',
            'b': '-...',
            'c': '-.-.',
            'd': '-..',
            'e': '.',
            'f': '',
            'g': '--.',
            'h': '....',
            'i': '..',
            'j': '.---',
            'k': '-.-',
            'l': '',
            'm': '--',
            'n': '',
            'o': '---',
            'p': '',
            'q': '...-',
            'r': '.-.',
            's': '...',
            't': '',
            'u': '',
            'v': '',
            'w': '',
            'x': '-..-',
            'y': '',
            'z': '',
        };

    def Translate(self, string text):
        result = ''
        for ch in text:
            try:
                result += self.table[ch]
            except KeyError:
                # Ignore letter not in the table
                pass
        return result
