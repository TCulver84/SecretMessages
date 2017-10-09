if __name__ == "__main__":

    import string
    from ciphers import Cipher


    class My_Keyword(Cipher):
        """Write a separate class, which inherits from cipher, and implements
        encrypt and decrypt functionality for each of your chosen ciphers."""


        def __init__(self, word="KRYPTOS"):
            self.word = word
            self.plaintext = string.ascii_uppercase
            self.rmv_txt = ''.join(c for c in self.plaintext if c not in self.word)
            self.encryptedtext = word + self.rmv_txt

        def encrypt(self, text):
            output = []
            text = text.upper()
            for char in text:
                try:
                    index = self.plaintext.index(char)
                except ValueError:
                    output.append(char)
                else:
                    output.append(self.encryptedtext[index])
            return ''.join(output)

        def decrypt(self, text):
            output = []
            text = text.upper()
            for char in text:
                try:
                    index = self.encryptedtext.index(char)
                except ValueError:
                    output.append(char)
                else:
                    output.append(self.plaintext[index])
            return ''.join(output)
