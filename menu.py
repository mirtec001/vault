from os import path
from generator import Generator
from diskops import DiskOperations


class Menu:

    def __init__(self):
        self.header_bar = ("==============================")
        self.quit = False


    def header(self):
        print(self.header_bar)
        print("     Pete's Vault     ")
        print(self.header_bar)

    def main_menu(self):
        print(self.header_bar)
        print("1. View Vault      2. Add Item")
        print("3. Delete Item     4. Quit    ")

    def add_item(self):
        print("Please enter a name for the entry")
        title = input(">> ")
        print("Please enter a username")
        username = input(">> ")
        print("Would you like a password generated?")
        answer = input(">> ")
        passkey = ""
        if answer == "y":
            print("Please enter length of the password")
            length = int(input(">> "))
            print("Numbers? ")
            num = input(">> ")
            print("Special characters? (y/n)")
            special_characters = input(">> ")

            accepted_passwd = "n"
            while accepted_passwd != "y":
                generated = Generator(length, num, special_characters).gen_pass()
                print(generated)
                print("Good password?")
                passkey = generated
                accepted_passwd = input(">> ")
        else:
            typed_answer = "n"
            while typed_answer != "y":
                print("Please enter you password")
                passkey = input(">> ")
                print("Good password?")
                typed_answer = input(">> ")

        self.review_input(title, username, passkey)
        print("Do you accept the info? (y/n)")
        answer = input(">> ")
        if answer == "y":
            DiskOperations().write_entry_to_disk(title, username, passkey)
        else:
            self.add_item()

    def review_input(self, title, username, password):
        print("Title: " + title)
        print("Username: " + username)
        print("Password: " + password)


    def view_vault(self):
        # Read the vault
        # and print them out here.
        vault = []
        if path.exists("vault.vlt"):
            vault = DiskOperations().read_vault()
            for x in range(len(vault)):
                print(vault[x])
        else:
            print("No vault exists.")

        print("Press enter to return to the main menu")
        input(">> ")
        self.main_menu()
