import socket
import struct
import binascii

class Network():

    def __init__ (self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost"
        self.port = 5050
        self.addr = (self.host, self.port)
        self.client.connect(self.addr)

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(2048).decode()

    def send(self, data):

        self.s = struct.Struct('4?')
        self.packed_data = self.s.pack(*data)

        self.client.send(self.packed_data)

       

    def get(self):

        self.s = struct.Struct('4?')
        packed_rcv_message = self.client.recv(self.s.size)
        unpacked_rcv_message = self.s.unpack(packed_rcv_message)
            
        return unpacked_rcv_message