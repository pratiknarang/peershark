from P2P_CONSTANTS import *

filenamelist = getCSVFiles(PCAPDATADIR)
outfile = open('back' , 'w')
for filename in filenamelist:
	inputfile = open(filename)
	starttime = float(inputfile.readline().split(',')[3])
	endtime = starttime
	for line in inputfile:
		endtime = float(line.split(',')[3])
	inputfile.close()
	outfile.write(
		filename + ',' +
		str(starttime) + ',' +
		str(endtime) + ',' +
		str((endtime-starttime)/(60*60)) + '\n')
outfile.close()