import socket
import sys
import time
from random import gauss

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print ('Failed to create socket')
	sys.exit()

# def getSettings(NumberOfFlow,WeightOfflow,IntervaltOfflow,LengthOfflow,NumberOfPacket):
# 	self.NOF=NumberOfFlow
# 	self.WOF=WeightOfflow
# 	self.IOF=IntervaltOfflow
# 	self.LOF=LengthOfflow
# 	self.NOP=NumberOfPacket
host = 'localhost'
port = 65431
NumberOfFlow=int(sys.argv[1])

NumberOfPacket = NOP[NumberOfFlow]
IntervaltOfflow=IOF[NumberOfFlow]
LengthOfPacket=packet_size[NumberOfFlow]
print("wwwwwwwwwwwwww")
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