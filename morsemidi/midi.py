class MIDI():
    pass

class VLQ():
    def __init__(self, input):
        if type(input) is int:
            self.num = input
        elif type(input) is bytes:
            self.num = self.bytesToNumber(input)

    def getBytes(self):
        return

    def getNumber(self):
        return self.num

    @staticmethod
    def numberToBytes(number):
        return b''

    @staticmethod
    def bytesToNumber(b):
        return 0