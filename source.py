import socket
import sys
import time
from random import gauss

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print ('Failed to create socket')
	sys.exit()

host = 'localhost'
port = 65431
NumberOfFlow=int(sys.argv[1])
IntervaltOfflow=float(sys.argv[2])
LengthOfPacket=int(sys.argv[3])
NumberOfPacket=int(sys.argv[4])
for j in range(NumberOfPacket):
	try:
		length=int(gauss(LengthOfPacket,50))
		if length < 0:
			length=LengthOfPacket
		msg = str(NumberOfFlow) +";{}".format(str(j + 1))+ ";{}".format(length) + ';packet {} from flow {} with length {}'.format(str(j + 1),NumberOfFlow,length)
		s.sendto(msg.encode('utf-8'), (host, port))
		print(msg)
	except (socket.error, msg):
		print ('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
		sys.exit()
	time.sleep(IntervaltOfflow)