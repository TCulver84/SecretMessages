if __name__ == "__main__":

    import string
    from ciphers import Cipher


    class AtBash(Cipher):
        """Write a separate class, which inherits from cipher, and implements
        encrypt and decrypt functionality for each of your chosen ciphers."""

        def __init__(self):
            self.FORWARD = string.ascii_uppercase
            self.BACKWARD = string.ascii_uppercase[::-1]

        def encrypt(self, text):
            output = []
            text = text.upper()
            for char in text:
                try:
                    index = self.FORWARD.index(char)
                except ValueError:
                    output.append(char)
                else:
                    output.append(self.BACKWARD[index])
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
                    output.append(self.FORWARD[index])
            return ''.join(output)
