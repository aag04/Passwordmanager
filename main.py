class PasswordManager:
    def __init__(self, master_password):
        self.master_password = master_password

    def encrypt(self, data):
        encrypted_data = []
        for char in data:
            encrypted_char = chr(ord(char) + len(self.master_password))
            encrypted_data.append(encrypted_char)
        return ''.join(encrypted_data)

    def decrypt(self, encrypted_data):
        decrypted_data = []
        for char in encrypted_data:
            decrypted_char = chr(ord(char) - len(self.master_password))
            decrypted_data.append(decrypted_char)
        return ''.join(decrypted_data)

    def store_password(self, website, username, password):
        data = f"Website: {website}\nUsername: {username}\nPassword: {password}"
        encrypted_data = self.encrypt(data)
        return encrypted_data

    def retrieve_password(self, encrypted_data):
        return self.decrypt(encrypted_data)

def main():
    master_password = input("Enter your master password: ")
    password_manager = PasswordManager(master_password)

    while True:
        print("\nPassword Manager")
        print("1. Store Password")
        print("2. Retrieve Password")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            encrypted_data = password_manager.store_password(website, username, password)
            print("Password stored successfully!")
            print("Encrypted Password Data:", encrypted_data)  # Print the encrypted data

        elif choice == "2":
            encrypted_data = input("Enter encrypted password data: ")
            decrypted_data = password_manager.retrieve_password(encrypted_data)
            print("Password Details:")
            print(decrypted_data)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
