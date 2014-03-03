import numpy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pylab
import os
import multiprocessing as MP
from P2P_CONSTANTS import *

def plotGraph(x, y, z, filename):
	v = [0,5000,0,200]
	plt.axis(v)
	plt.scatter(x, y, alpha = 0.10, cmap=plt.cm.cool, edgecolors='None')
	# plt.colorbar()
	pylab.savefig(filename, bbox_inches = 0)
	plt.clf()

#scale input data and plot graphs
def processFile(filename):
	sem.acquire()
	
	x1 = []
	# x2 = []
	y = []
	z = []
	
	inputfile = open(filename)
	for line in inputfile:
		fields = line.strip().split(',')
		x1.append(float(fields[3]) / 1000)		
		# x2.append(float(fields[3]) / (1000 * int(fields[2])))
		y.append(float(fields[-1]) / 1000)
		z.append(float(fields[4]) / 1000)
	inputfile.close()
	
	filename = filename.split('/')
	outputdir = NEWDIR + filename[-2] + '/'
	if not os.path.exists(outputdir):
		os.makedirs(outputdir)

	plotGraph(x1, y, z, outputdir + filename[-1] + '.png')
	# plotGraph(x2, y, z, filename + 'modified.png')
	print 'Completed plotting ' + '/'.join(filename)

	sem.release()

NEWDIR = SUPERFLOWDATADIR + 'alphachanged/'
if not os.path.exists(NEWDIR):
	os.makedirs(NEWDIR)
folders = os.listdir(SUPERFLOWDATADIR)
csvfiles = []
for eachname in folders:
	name = SUPERFLOWDATADIR + eachname +'/'
	if os.path.isdir(name):
		csvfiles += getCSVFiles(name)

print csvfiles

sem = MP.Semaphore(THREADLIMIT)
for eachfile in csvfiles:
	task = MP.Process(target = processFile, args = (eachfile,))
	task.start()
