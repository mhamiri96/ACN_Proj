WeightOfflows=[]
IntervaltOfflows=[]
LengthOfflows=[]
NumberOfPackets=[]
flowInfo={}

def getInfo():
    # print("Number of flows: ")
    WeightOfflows=[]
    IntervaltOfflows=[]
    LengthOfflows=[]
    NumberOfPackets=[]
    global flowInfo
    file = open('init.csv','r')
    content = file.readlines()
    NumberOfFlows=int(len(content))
    for i in range(len(content)):
        tmp=content[i].split(',')
        print("Weight of flow {}: ".format(i))
        tempW=int(tmp[0])
        WeightOfflows.append(tempW)
        print(tempW)
        print("Average time interval of packets in flow {}: ".format(i))
        tempTI=float(tmp[2])
        IntervaltOfflows.append(tempTI)
        print(tempTI)
        print("Average length of packets in flow {}: ".format(i))
        tempLP=int(tmp[3])
        LengthOfflows.append(tempLP)
        print(tempLP)
        print("Number of packets in flow {}: ".format(i))
        tempNP=int(tmp[4])
        NumberOfPackets.append(tempNP)
        print(tempNP)
        tmp={i:{'NumberOfPacket':tempNP,'IntervaltOfflow':tempTI,'LengthOfPacket':tempLP}}
        flowInfo |=tmp
    
    return flowInfo,LengthOfflows,WeightOfflows,NumberOfFlows,IntervaltOfflows,NumberOfPackets
getInfo()