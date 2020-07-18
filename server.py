import socket

class Server():

    def __init__ (self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost"
        self.port = 5050
        self.addr = (self.host, self.port)

    def connect(self):
        self.server.bind(self.addr)
        self.server.listen()
        self.conn , self.address =  self.server.accept()


    def send(self, data):
        self.conn.send(str.encode(data))
        rcv_message = self.conn.recv(2048).decode()
        return rcv_message


 #   server.bind(ADDR)
 #   server.listen()
 #   conn, addr =  server.accept()
 #   print('Server Connected')
 #   connected = True
 #   while connected:
 #       message = input('Type Your Message : ') 
 #       conn.send(message.encode())
 #       rcv_message = conn.recv(2048).decode()
 #       print ('CLIENT:', rcv_message)
 #       if rcv_message == DISCONNECT_MSG:
 #           connected = False
 #   conn.close()


