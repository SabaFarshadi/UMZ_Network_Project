import socket
import struct
import binascii

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

        self.s = struct.Struct('4?')
        self.packed_data = self.s.pack(*data)
        self.conn.send(self.packed_data)

    def get(self):
        
        self.s = struct.Struct('4?')
        packed_rcv_message = self.conn.recv(self.s.size)
        unpacked_rcv_message = self.s.unpack(packed_rcv_message)

        return unpacked_rcv_message


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


