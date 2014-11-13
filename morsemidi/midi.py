class MIDI():
    pass

class VLQ():
    def __init__(self, input):
        self.num = input

    def getBytes(self):
        return self.numberToBytes(self.num)

    def getNumber(self):
        return self.num

    @staticmethod
    def numberToBytes(num):
        lst = []
        first = True
        while num > 0:
            lst.insert(0, (num & 0x7F) | (0x80 if not first else 0x00))
            num >>= 7
            first = False

        return b''.join([chr(x) for x in lst]).rjust(4, '\x00')[-4:]