from cryptography.fernet import Fernet

# Generate a new encryption key
key = Fernet.generate_key()

# Save it securely (do NOT share with hostile ships!)
with open("secret.key", "wb") as key_file:
    key_file.write(key)

print("🔑 Secret key generated! Keep this safe.")
