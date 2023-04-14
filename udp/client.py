import socket
import random
import time

def create_client():

	bufferSize  = 1024
	serverIP     = "127.0.0.1"
	serverPort   = 7500

	localIP     = "127.0.0.1"
	localPort   = 7501

	# Create datagram socket
	UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
	UDPClientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


	message = "From Client To Server"
	UDPClientSocket.sendto(message.encode(), (serverIP, serverPort))

	UDPClientSocket.close()
	UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

	UDPClientSocket.bind((localIP, localPort))
	return UDPClientSocket

def run_client(UDPClientSocket, q):
		
	bufferSize  = 1024
	localIP     = "127.0.0.1"
	localPort   = 7501

	print(f'UDP client up and lisLtening on {localIP}:{localPort}')

	count = 0
	while count < 10:
		message, _ = UDPClientSocket.recvfrom(bufferSize)
		print(f'client recieved message {message.decode()}')
		count += 1

	print("program complete")

#create_client()