PCAPDATADIR = './pcapdata/'
FLOWDATADIR = './flowdata/'
SUPERFLOWDATADIR = './superflowdata/'
TRAININGDIR = './training/'
PCAPFILES = 'PcapInputFiles.txt'
TSHARKOPTIONSFILE = 'TsharkOptions.txt'
FLOWOPTIONS = 'FlowOptions.txt'
FLOWOUTFILE = PCAPDATADIR + 'FLOWDATA'
C_FLOWOUTFILE = PCAPDATADIR + 'COMPLETEFLOWDATA'
FLOWGAP = 1 * 60 * 60
THREADLIMIT = 10
TCP_PROTO = '6'
UDP_PROTO = '17'
UDP_HEADERLENGTH = 8

#utility functions
import os
def getCSVFiles(dirname):
	csvfiles = []
	for eachfile in os.listdir(dirname):
		if eachfile.endswith('.csv'):
			csvfiles.append(dirname + eachfile)	
	return csvfiles