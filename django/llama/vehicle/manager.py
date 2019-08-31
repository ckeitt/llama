import socket
import time

class VehicleSocketManager:

    def __init__(self, public_ip_address, port):
        self.public_ip_address = public_ip_address
        self.port = port

    def unlock_vehicle(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((str(self.public_ip_address), int(self.port)))
        time.sleep(1)
        s.send(b'0')
        time.sleep(1)
        s.shutdown(socket.SHUT_WR)
