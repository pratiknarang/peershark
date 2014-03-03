from P2P_CONSTANTS import *
import socket
import Flow
import SuperFlow
import sys

try:
	starttime = int(sys.argv[1]) * 60 * 60
	increment = int(sys.argv[2]) * 60 * 60
	endtime = int(sys.argv[3]) * 60 * 60
except:
	print 'Incorrect Arguments to Module'
	print 'Correct Format:'
	print 'python generateSuperFlows.py start(hrs) increment(hrs) end(hrs)'
	exit()

if starttime > endtime:
	print 'Start should be less than end'
	exit()

csvfiles = getCSVFiles(FLOWDATADIR)
print csvfiles

flowdata = []
for filename in csvfiles:
	inputfile = open(filename)
	data = [line.strip() for line in inputfile]
	inputfile.close()

	for eachline in data:
		fields = eachline.split(',')
		flowdata.append(SuperFlow.SuperFlow(fields))
print 'No. of flows to be processed: ' + str(len(flowdata))

while starttime <= endtime:
	flowdata = Flow.combineFlows(flowdata, starttime)
	print 'No. of flows with timegap = ' + str(starttime) + 'sec : ' + str(len(flowdata))

	outfile = open(SUPERFLOWDATADIR + str(starttime) + '.csv', 'w')
	for flow in flowdata:
		outfile.write(
			socket.inet_ntoa(flow.ip1) + ',' +
			socket.inet_ntoa(flow.ip2) + ',' +
			str(flow.getNoOfPackets()) + ',' +
			str(flow.getNoOfBytes()) + ',' +
			'%.6f'%flow.getInterArrivaltime() + ',' +
			'%.6f'%flow.getStart() + ',' +
			'%.6f'%flow.getEnd() + ',' +
			'%.6f'%flow.getDurationInSeconds() + '\n')
	outfile.close()
	
	starttime += increment