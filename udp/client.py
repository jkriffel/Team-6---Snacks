import socket
import random
import time

bufferSize  = 1024
serverAddressPort   = ("127.0.0.1", 7500)

# Create datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

message = "Message received"
UDPServerSocket.sendto(str.encode(str(message)), serverAddressPort)
time.sleep(random.randint(1,3))
	
print("program complete")