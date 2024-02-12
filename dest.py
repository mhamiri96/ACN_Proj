import socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
except socket.error:
	print ('Failed to create socket')
	sys.exit()
 
host = 'localhost'
port = 65431
temp="-1;dest"
s.sendto(temp.encode('utf-8'), (host, port))
while True:
	try:
		d = s.recvfrom(2048)
		reply =d[0]
		addr = d[1]
		print ('Server reply : ' + reply.decode())
	except (socket.error, msg):
		print ('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
		sys.exit()