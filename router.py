import socket
import sys
import time
import threading
from main import getInfo

HOST = '127.0.0.1'
PORT = 65431

current_milli_time = lambda: int(round(time.time() * 1000))

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	print ('Socket created')
except (socket.error, msg):
	print ('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()

try:
	s.bind((HOST, PORT))
except (socket.error , msg):
	print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()
	
print ('Socket bind complete')
daddr = None
roundNumber = 0
activeConn = 0
source={}
flowInfo,LengthOfFlows,WeightOfFlows,NumberOfFlows,IntervaltOfFlows,NumberOfPackets=getInfo()
for i in range(0,NumberOfFlows):
	temp = {i:{'time':[],'data':[], 'fno':[], 'active':0, 'sent':[0]}}
	source |=temp
print(source)
count = 0
sleeptime=0.01
daddr=None
globalTime = None
flag = 0
rDash = 0

def recvpacket():
	global source
	global flag
	global rDash
	while True:
		d = s.recvfrom(1024)
		recvTime = current_milli_time()
		if len(d[0].decode().split(';'))==2:
			fromSource, data=d[0].decode().split(';')
		else:
			fromSource,NumOfPack,rleng,data = d[0].decode().split(';')
		fromSource = int(fromSource)
		if data == "dest":
			global daddr
			daddr= d[1]
			s.sendto(('connection established').encode('utf-8'),daddr)
			continue
		if flag == 0:
			prevTime = 0
			globalTime = recvTime
			roundNumber = 0
			flag = 1
		if len(source[fromSource]['fno']) == 0:
			print ('First packet')
			fno = roundNumber + (LengthOfFlows[fromSource]*1.0/WeightOfFlows[fromSource])
			source[fromSource]['fno'].append(fno)
		else:
			len(source[fromSource]['fno'])
			print ('length', len(source[fromSource]['fno']), 'source', fromSource)
			fno = max(roundNumber, source[fromSource]['fno'][len(source[fromSource]['fno']) - 1]) + (LengthOfFlows[fromSource]*1.0/WeightOfFlows[fromSource])
			source[fromSource]['fno'].append(fno)
		source[fromSource]['time'].append(recvTime - globalTime)
		source[fromSource]['data'].append(str(fromSource) + ';' + data)
		source[fromSource]['sent'].append(0)
		roundNumber += ((recvTime - globalTime) - prevTime)*rDash
		lFno = max(source[fromSource]['fno'])
		print (lFno, roundNumber)
		if lFno > roundNumber:
			source[fromSource]['active'] = 1
		else:
			source[fromSource]['active'] = 0
		weightsSum = 0
		for i in range(NumberOfFlows):
			if source[i]['active'] == 1:
				weightsSum += WeightOfFlows[i]
		if weightsSum == 0:
			continue
		rDash = 1.0/weightsSum
		prevTime = recvTime - globalTime
	s.close()

def sendpacket():
	while True:
		if daddr:
			mini = 999999999999999
			index = 0
			so = 0
			for i in range(NumberOfFlows):
				for j in range(len(source[i]['fno'])):
					if source[i]['sent'][j] == 0:
						if source[i]['fno'][j] < mini:
							mini = min(source[i]['fno'])
							index = j
							so = i
			if mini != 999999999999999:
				s.sendto(source[so]['data'][index].encode('utf-8'), daddr)
			source[so]['sent'][index] = 1
			time.sleep(sleeptime)

t1 = threading.Thread(target=recvpacket)
t1.daemon = True
t2 = threading.Thread(target=sendpacket)
t2.daemon = True

t1.start()
t2.start()

while threading.active_count() > 0:
    time.sleep(0.1)