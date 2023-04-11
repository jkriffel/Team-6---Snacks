import socket
import random
import time
import json 

def random_traffic():
	bufferSize  = 1024
	serverAddressPort   = ("127.0.0.1", 7501)

	# Importing the player data from Json file
	with open("table_data.json", "r") as file:
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

	# Create datagram socket
	UDPClientSocketTransmit = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

	# counter number of events, random player and order
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

		print(message)
		i+=1;
		UDPClientSocketTransmit.sendto(str.encode(str(message)), serverAddressPort)
		time.sleep(random.randint(1,3))
		
	print("program complete")