import socketserver

class ClientHandler(socketserver.baseRequestHandler):

    def handle(self):
        encrypted_key = self.request.recv(1024).strip()
        print("Implement decryption of data " + encrypted_key)
        #----------------------------------
        #   Decryption Code Here
        #----------------------------------

        self.request.sendall("Send key back")


if __name__ == "__main__":
    HOST,PORT = "", 8000

    tcpServer = socketserver.TCPServer((HOST,PORT), Clienthandler)
    try:
        tcpServer.serve_forever()
    except:
        print("There was an error")
