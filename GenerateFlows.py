from P2P_CONSTANTS import *
from Packet import *
from Flow import *
import multiprocessing as MP
import socket

## module to read all the files in the data folder of the 
## project, build flow data and store it in a file

def generateFlow(filename):
	sem.acquire()
	
	inputfile = open(filename)
	data = [line.strip() for line in inputfile]
	inputfile.close()
		
	packetlist = []
	for eachline in data:
		fields = eachline.split(',')
		fields.pop(2)
		packetlist.append(Packet(fields))
	
	outflowlist = packetsToFlows(packetlist, FLOWGAP)
	print 'flows in ' + filename + ' : ' + str(len(outflowlist))
	
	outfilename = FLOWDATADIR + (filename.split('/')[-1])		
	writeFlowsToFile(outflowlist, outfilename)

	print 'done writing to : ' + outfilename
	sem.release()

csvfiles = getCSVFiles(PCAPDATADIR)
print csvfiles

#create a semaphore so as not to exceed threadlimit
sem = MP.Semaphore(THREADLIMIT)

#generate flowdata from each input packet file(not pcap) in parallel and store it in a file
#so we get as many output files as number of input files
for filename in csvfiles:
	task = MP.Process(target = generateFlow, args = (filename,))
	task.start()

# #execute commands in parallel
# for task in tasklist:
# 	sem.acquire()
# 	task.start()

# #wait for tasks to finish
# for task in tasklist:
# 	task.join()

# allflows = [flow for flowlist in alloutflowlists for flow in flowlist]
# finalflows = []
# combineFlows(allflows, FLOWGAP, finalflows)

# outfile = open(C_FLOWOUTFILE, 'w')
# for flow in finalflows:
# 	outfile.write(socket.inet_ntoa(flow.ip1) + ',' +
# 		socket.inet_ntoa(flow.ip2) + ',' +
# 		str(flow.getNoOfPackets()) + ',' +
# 		str(flow.getNoOfBytes()) + ',' +
# 		'%.6f'%flow.getInterArrivaltime() + ',' +
# 		'%.6f'%flow.getStart() + ',' +
# 		'%.6f'%flow.getEnd() + ',' +
# 		'%.6f'%flow.getDurationInSeconds() + ',' +
# 		str(flow.n_packet1) + ',' +
# 		str(flow.n_byte1) + ',' +
# 		'%.6f'%flow.t_start1 + ',' +
# 		'%.6f'%flow.t_end1 + ',' +
# 		'%.6f'%flow.getInterArrivaltime1() + ',' +
# 		str(flow.n_packet2) + ',' +
# 		str(flow.n_byte2) + ',' +
# 		'%.6f'%flow.t_start2 + ',' +
# 		'%.6f'%flow.t_end2 + ',' +
# 		'%.6f'%flow.getInterArrivaltime2() + '\n')
# outfile.close()
