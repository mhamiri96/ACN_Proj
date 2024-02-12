import socket
import sys
import time
import threading
from main import getInfo

HOST = '127.0.0.1'
PORT = 65431

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

from main import getInfo
roundNumber = 0
queues={}
flowInfo,LengthOfFlows,WeightOfFlows,NumberOfFlows,IntervaltOfFlows,NumberOfPackets=getInfo()
for i in range(0,NumberOfFlows):
	temp = {i:{'time':[],'data':[], 'finishNum':[], 'active':0, 'sent':[0],'NumOfPacket':[]}}
	queues |=temp

sleeptime=0.01
addr=None
globalTime = None
flag = 0
reversedWeights = 0
currentTime = lambda: int(round(time.time() * 1000))

def recvpacket():
	global queues
	global flag
	global reversedWeights
	while True:
		d = s.recvfrom(2048)
		recvTime = currentTime()
		if len(d[0].decode().split(';'))==2:
			fromSource, data=d[0].decode().split(';')
		else:
			fromSource,NumOfPack,recvLen,data = d[0].decode().split(';')
		fromSource = int(fromSource)
		if data == "dest":
			global addr
			addr= d[1]
			s.sendto(('connection established').encode('utf-8'),addr)
			continue
		if flag == 0:
			prevTime = 0
			globalTime = recvTime
			roundNumber = 0
			flag = 1
		if len(queues[fromSource]['finishNum']) == 0:
			print ('First packet')
			finishNum = roundNumber + (int(recvLen)*1.0/WeightOfFlows[fromSource])
			queues[fromSource]['finishNum'].append(finishNum)
		else:
			print ('Finish Number: ', len(queues[fromSource]['finishNum']), ' from flow: ', fromSource)
			finishNum = max(roundNumber, queues[fromSource]['finishNum'][len(queues[fromSource]['finishNum']) - 1]) + (int(recvLen)*1.0/WeightOfFlows[fromSource])
			queues[fromSource]['finishNum'].append(finishNum)
		queues[fromSource]['time'].append(recvTime - globalTime)
		queues[fromSource]['data'].append(str(fromSource) + ';' + data)
		queues[fromSource]['sent'].append(0)
		queues[fromSource]['NumOfPacket'].append(NumOfPack)
		roundNumber += ((recvTime - globalTime) - prevTime)*reversedWeights
		lfinishNum = max(queues[fromSource]['finishNum'])
		print ('Latest Finish Number: ', lfinishNum, ' Round Number: ', roundNumber)
		if lfinishNum > roundNumber:
			queues[fromSource]['active'] = 1
		else:
			queues[fromSource]['active'] = 0
		SumOfWeight = 0
		# checking if some connection becomes inactive
		for i in range(NumberOfFlows):
			if queues[i]['active'] == 1:
				SumOfWeight += WeightOfFlows[i]
		if SumOfWeight == 0:
			continue
		reversedWeights = 1.0/SumOfWeight
		prevTime = recvTime - globalTime
	s.close()

def sendpacket():
	while True:
		if addr:
			mini = 99999999
			index = 0
			temp = 0
			# transmit from lowest finish number list
			for i in range(NumberOfFlows):
				for j in range(len(queues[i]['finishNum'])):
					if queues[i]['sent'][j] == 0:
						if queues[i]['finishNum'][j] < mini:
							mini = min(queues[i]['finishNum'])
							index = j
							temp = i
			if mini != 99999999:
				s.sendto(queues[temp]['data'][index].encode('utf-8'), addr)
			queues[temp]['sent'][index] = 1
			time.sleep(sleeptime)

t1 = threading.Thread(target=recvpacket)
t1.daemon = True
t2 = threading.Thread(target=sendpacket)
t2.daemon = True
t1.start()
t2.start()
while threading.active_count() > 0:
    time.sleep(0.1)