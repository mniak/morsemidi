class Morse():
    def __init__(self):
        self.table = {
            'a': '.-',
            'b': '-...',
            'c': '-.-.',
            'd': '-..',
            'e': '.',
            'f': '..-.',
            'g': '--.',
            'h': '....',
            'i': '..',
            'j': '.---',
            'k': '-.-',
            'l': '.-..',
            'm': '--',
            'n': '-.',
            'o': '---',
            'p': '.--.',
            'q': '--.-',
            'r': '.-.',
            's': '...',
            't': '-',
            'u': '..-',
            'v': '...-',
            'w': '.--',
            'x': '-..-',
            'y': '-.--',
            'z': '--..',
        };

    def translate(self, text):
        if len(text) > 1:
            return ';'.join((','.join((self.translate(l) for l in w)) for w in text.split()))
        elif self.table.has_key(text):
            return self.table[text]
        else:
            return ''