Synopsis

Most of us have, at one time or another, wanted to pass messages to our friends that other people couldn't read. Maybe it was a note in class, a midnight rendezvous, or something more serious like invasion plans. Whatever the purpose, you'd want your message to be encoded so only the people you want to can read it. That's where ciphers come in!

Ciphers are repeatable ways to encode a message. One of the most famous is the Caesar Cipher, used by Julius Caesar for his private communications. He would take each letter of the message and change it to the letter that was three characters further on in the Roman alphabet. For example, if I was going to encode the word "dog", using the American English alphabet, I would change the "d" to "g", which is three letters further on. The "o" would become "r", and the "g" turns into "j". Instead of sending "dog" to my friend, I'd send "grj". To figure it out, my friend would move each letter back three characters.

One thing Julius Caesar didn't have, though, is a computer to do all of this encoding and decoding for him!


Code Example

The code library contains 1 application that refers to multiple subclasses of the parent class Cipher.

The application itself references each ciphe subclass as a unique instance and can encrypt/decrypt based on user selection of the various classes.

For Example - main.py

Each cipher subclass is assigned to the variable klass, so when referenced below in the execution of the transformation of the text klass.encrypt and klass.decrypt are variable to a user's input

        if cipher in available_ciphers:
            if cipher.lower() == 'caesar':
                klass = Caesar()
            elif cipher.lower() == 'affine':
                klass = Affine()
            elif cipher.lower() == 'atbash':
                klass = AtBash()
            elif cipher.lower() == 'keyword':
                print("\n{} is a good cipher!\n".format(cipher.title()))
        elif cipher not in available_ciphers:
            print("\nThat's not an availble cipher, please select again!\n")
            continue
        else:
            pass
        user_choice = input("Are we going to encrypt or decrypt? ")
        if user_choice.lower() == 'encrypt':
            cipher_text = input("\nWhat cipher text do you want to encrypt? ")
            print('\n', klass.encrypt(str(cipher_text)))
        elif user_choice.lower() == 'decrypt':
            cipher_text = input("\nWhat cipher text do you want to decrypt? ")
            print('\n', klass.decrypt(str(cipher_text)))
        else:
            continue

For Example - affine.py

class Affine(Cipher):

the cipher Affine is calling the parent class Cipher()

    def __init__(self):
        self.ALPHA = string.ascii_uppercase

The encrypt method takes an empty list, and shifts the index location of a value in a string. For example below, for the string 'APPLE' the letter a would be at index value 0, the encryption shifts this value to 8 representing the letter 'I' which would result in the cipher text being returned 'IFFLC'

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

Similar to above, the decrypt method reverses the pattern by indexing the value of the character in the string to it's originial value. 'IFFLC' becomes 'APPLE' and so on.

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


Motivation

The motivation for this project was to be able to encrypt and decrypt string text using a variety of different ciphers, by doing so it gave me the opportunity to understand how to reference different classes with similar functionality in the program.


Installation

To install the project download all files to a location of your choosing on your computer, log into the terminal (on a MAC) and instantiate the program from the directory where you stored the files as follows:

python3 -i main.py


Tests

To test this application enter in the choice variable for the cipher (i.e. Caesar), chose to encrypt or decrypt a cipher text and then enter the string value of your choosing to be encrypted/decrypted. The program will give you the option to continue or exit thereafter.


Contributors

This project was inspired by the teachers at teamtreehouse.com and was developed by Taylor.


License

Opensource for your enjoyment!