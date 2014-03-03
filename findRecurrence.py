from P2P_CONSTANTS import *
from Packet import *
from Flow import *
import threading
import socket
import os

#CAN SAFELY IGNORE THIS FILE

csvfiles = []
for eachfile in os.listdir(DATADIR):
	if eachfile.endswith('.csv'):
		csvfiles.append(DATADIR + eachfile)

packetdict = dict()

for inputfilename in csvfiles:
	inputfile = open(inputfilename)
	data = [line.strip() for line in inputfile]
	inputfile.close()
	
	packetlist = []
	for eachline in data:
		fields = eachline.split(',')
		fields.pop(2)
		packetlist.append(Packet(fields))

	for each in packetlist:
		if packetdict.has_key(each.key):
			packetdict[each.key][2].add(inputfilename)
		else:
			packetdict[each.key]=(socket.inet_ntoa(each.source),socket.inet_ntoa(each.dest),{inputfilename})

for each in packetdict:
	print packetdict[each]
