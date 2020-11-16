

class DiskOperations:

    def write_entry_to_disk(self, title, username, password):
        with open("vault.vlt", "a") as fw:
            fw.write(title + "," + username + "," + password)

    def read_vault(self):
        with open("vault.vlt", "r") as fr:
                vault = fr.readlines()
                
        return vault
