import socket
import random
import time
import json

def start_server():
	# Sets variables to holdsocket info
	localIP     = "127.0.0.1"
	localPort   = 7500
	bufferSize  = 1024

	# Create a datagram socket
	UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
	UDPServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	# Bind to address and ip
	UDPServerSocket.bind((localIP, localPort))

	print(f'UDP server up and listening on {localIP}:{localPort}')

	# Listen for incoming datagrams
	bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

	#close the socket this required don't ask
	UDPServerSocket.close()
	del UDPServerSocket
	print(f'{bytesAddressPair}: message recieved and server closed')

	with open("table_data.json") as file:
			team_data = json.load(file)
	green_team_data = team_data[0]
	red_team_data = team_data[1]

	#Making a list of both teams IDs
	greenID = []
	for i in green_team_data:
		greenID.append(i)
	green1 = str(greenID[0])
	green2 = str(greenID[1])

	redID = []
	for i in red_team_data:
		redID.append(i)
	red1 = str(redID[0])
	red2 = str(redID[1])

	# Generating a number of events 
	num_events = random.randint(10,20)

	# create the socket again... don't ask
	UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

	for i in range(1, int(num_events)):
		if random.randint(1,2) == 1:
			red_player_ID = red1
			red_player_name = red_team_data[redID[0]]
		else:
			red_player_ID = red2
			red_player_name = red_team_data[redID[1]]

		if random.randint(1,2) == 1:
			green_player_ID = green1
			green_player_name = green_team_data[greenID[0]]
		else: 
			green_player_ID = green2
			green_player_name = green_team_data[greenID[1]]	

		# Make these messages cool 

		if random.randint(1,2) == 1:
			message = red_player_name + " Lasered " + green_player_name
		else:
			message = green_player_name + " Lasered " + red_player_name

		# Rather than printing to console, put into action screen
		print(message)
		UDPServerSocket.sendto(str.encode(str(message)), (localIP, 7501))
		time.sleep(random.randint(1,3))

#start_server()