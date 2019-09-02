import socket
import time

class VehicleSocketManager:

    def __init__(self, public_ip_address, port, access_key):
        self.public_ip_address = public_ip_address
        self.port = port
        self.access_key = access_key
        
    def unlock_vehicle(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((str(self.public_ip_address), int(self.port)))
        time.sleep(0.5)
        s.send(b'%s0' % self.access_key)
        time.sleep(1)
        s.shutdown(socket.SHUT_WR)
