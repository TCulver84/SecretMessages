import string

from ciphers import Cipher


class Caesar(Cipher):
    """Write a separate class, which inherits from cipher, and implements
    encrypt and decrypt functionality for each of your chosen ciphers."""
    FORWARD = string.ascii_uppercase * 3

    def __init__(self, offset=3):
        self.offset = offset
        self.ALPHA = string.ascii_uppercase
        self.FORWARD = self.ALPHA + self.ALPHA[:self.offset+1]
        self.BACKWARD = self.ALPHA[:self.offset+1] + self.ALPHA

    def encrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.FORWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.FORWARD[index+self.offset])
        return ''.join(output)

    def decrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.BACKWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.BACKWARD[index-self.offset])
        return ''.join(output)
