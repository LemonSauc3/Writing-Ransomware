import socketserver
from cryptography.fernet import Fernet

class ClientHandler(socketserver.BaseRequestHandler):

    def handle(self):
        encrypted_key = self.request.recv(1024).strip()
        #----------------------------------
        
        f = Fernet(encrypted_key.decode())
        decrypted_key = f.decrypt(encrypted_key)
        print(decrypted_key.decode())
        #----------------------------------

        self.request.sendall(decrypted_key)


if __name__ == "__main__":
    HOST,PORT = "127.0.0.1", 8000
    print("Starting Server")
    tcpServer = socketserver.TCPServer((HOST,PORT), ClientHandler)
    try:
        tcpServer.serve_forever()
    except:
        print("There was an error")
