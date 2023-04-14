import socket
import random
import time
import json

# Sets variables to holdsocket info
localIP     = "127.0.0.1"
localPort   = 7500
bufferSize  = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams
bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
#message = bytesAddressPair[0]
#clientMsg = message

print(bytesAddressPair)

with open("table_data.json") as file:
    team_data = json.load(file)
# Seperating the teams
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
counter = random.randint(10,20)

# Creates datagram to send to socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

i = 1
while i < int(counter):
	if random.randint(1,2) == 1:
		redplayer = red1
		codeRName = red_team_data[redID[0]]
	else:
		redplayer = red2
		codeRName = red_team_data[redID[1]]

	if random.randint(1,2) == 1:
		greenplayer = green1
		codeGName = green_team_data[greenID[0]]
	else: 
		greenplayer = green2
		codeGName = green_team_data[greenID[1]]	

	# Make these messages cool 

	if random.randint(1,2) == 1:
		message = codeRName + " Lasered " + codeGName
	else:
		message = codeGName + " Lasered " + codeRName

	i+=1
	# Rather than printing to console, put into action screen
	print(message)
	UDPServerSocket.sendto(str.encode(str(message)), (localIP, localPort))
	time.sleep(random.randint(1,3))