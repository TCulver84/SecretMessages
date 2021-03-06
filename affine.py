import string
from ciphers import Cipher


class Affine(Cipher):

    def __init__(self):
        self.ALPHA = string.ascii_uppercase

    def encrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                index = ((self.ALPHA.index(char) * 5) + 8) % 26
            except ValueError:
                output.append(char)
            else:
                output.append(self.ALPHA[index])
        return ''.join(output)

    def decrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                index = (21 * (self.ALPHA.index(char) - 8) % 26)
            except ValueError:
                output.append(char)
            else:
                output.append(self.ALPHA[index])
        return ''.join(output)
