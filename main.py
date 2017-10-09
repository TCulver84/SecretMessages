if __name__ == "__main__":

    from caesar import Caesar
    from my_keyword import My_Keyword
    from affine import Affine
    from ciphers import Cipher
    from atbash import AtBash
    import os


    def menu():
        """Provide a command line menu providing an option to either encrypt or
        decrypt a value and then a sub menu with a list of implemented
        ciphers"""
        os.system('clear')
        print("This is the Secret Messages project by Taylor Culver.\n")
        print("These are the Current available ciphers:\n")
        print("-Caesar\n-Affine\n-Atbash\n-Keyword")


    def game_loop():
        """Prompt the user for input to encrypt or decrypt and, if applicable,
        any additional input settings required to perform the
        cipher process."""
        menu()
        while True:
            cipher = input("\nWhich cipher would you like to use? ").title()
            available_ciphers = ["Caesar", "Affine", "Atbash", "Keyword"]
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
            value = input("\nEncrypt/decrypt something else? (Y/N) ")
            if value.lower() == 'y':
                menu()
                continue
            elif value.lower() == 'n':
                print("\nThanks for using the Secret Messages app!!!\n")
                break
            else:
                pass

    game_loop()
