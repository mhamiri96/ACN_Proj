WeightOfflows=[]
IntervaltOfflows=[]
LengthOfflows=[]
NumberOfPackets=[]
flowInfo={}

def getInfo():
    print("Number of flows: ")
    NumberOfFlows=int(input())
    WeightOfflows=[]
    IntervaltOfflows=[]
    LengthOfflows=[]
    NumberOfPackets=[]
    global flowInfo
    for i in range(NumberOfFlows):
        print("Weight of flow {}: ".format(i))
        tempW=int(input())
        WeightOfflows.append(tempW)
        print("Average time interval of packets in flow {}: ".format(i))
        tempTI=float(input())
        IntervaltOfflows.append(tempTI)
        print("Average length of packets in flow {}: ".format(i))
        tempLP=int(input())
        LengthOfflows.append(tempLP)
        print("Number of packets in flow {}: ".format(i))
        tempNP=int(input())
        NumberOfPackets.append(tempNP)
        tmp={i:{'NumberOfPacket':tempNP,'IntervaltOfflow':tempTI,'LengthOfPacket':tempLP}}
        flowInfo |=tmp
    return flowInfo,LengthOfflows,WeightOfflows,NumberOfFlows,IntervaltOfflows,NumberOfPackets