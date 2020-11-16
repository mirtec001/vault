import getpass

class Lock:

    def unlock(self):
        print("Please enter you username")
        username = input(">> ")

        print("Please enter your password")
        passwd = getpass.getpass(">> ")

        if self.validiate_input(username, passwd):
            print("Unlocked")
            return False
        else:
            print("Invalid username or password")
            return True

    def validiate_input(self, username, passwd):
        if username == "user":
            if passwd == "abc123":
                return True
            else:
                return False
        else:
            return False