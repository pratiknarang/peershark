from P2P_CONSTANTS import *
DATALIMIT = 50000

#takes takes 50,000 examples and puts it in necessary format for training
folders = os.listdir(SUPERFLOWDATADIR)
csvfiles = []
for eachname in folders:
	name = SUPERFLOWDATADIR + eachname +'/'
	if os.path.isdir(name):
		csvfiles += getCSVFiles(name)

outfile = open(TRAININGDIR + 'trainingdata1.csv','w')
for filename in csvfiles:
	label = filename.split('/')[-2]
	inputfile = open(filename)
	count = DATALIMIT - 1
	line = inputfile.readline().strip()
	while count > 0 and line!='':
		fields = line.split(',')
		if float(fields[4])!=0 and float(fields[3])!=0 and float(fields[7])!=0:
			outfile.write(
				fields[2] + ',' +
				fields[3] + ',' +
				fields[4] + ',' +
				fields[7] + ',' +
				label + '\n')
			count -= 1
		line = inputfile.readline().strip()
	inputfile.close()
	print DATALIMIT - count
outfile.close()
