from cryptography.fernet import Fernet

# Generate and save the key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as 'secret.key'.")

# Load the existing key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt the file using the key
def encrypt_file(file_name):
    key = load_key()
    f = Fernet(key)
    
    with open(file_name, "rb") as file:
        file_data = file.read()
        
    encrypted_data = f.encrypt(file_data)
    
    with open(file_name + ".encrypted", "wb") as file:
        file.write(encrypted_data)
        
    print(f"Encrypted file saved as {file_name}.encrypted!")

# Decrypt the file using the key
def decrypt_file(file_name):
    key = load_key()
    f = Fernet(key)
    
    with open(file_name, "rb") as file:
        encrypted_data = file.read()
        
    decrypted_data = f.decrypt(encrypted_data)
    
    with open(file_name + ".decrypted", "wb") as file:
        file.write(decrypted_data)
        
    print(f"Decrypted file saved as {file_name}.decrypted!")

# Main program logic
if __name__ == "__main__":
    generate_key()  # This will generate the 'secret.key' file.
    encrypted_file = encrypt_file("secret.txt")
    decrypted_file = decrypt_file("secret.txt.encrypted")
