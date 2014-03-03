PeerShark: Peer-to-Peer botnet detection by tracking conversations.
This was developed by a Subhajit Ray. Since he did not upload it publicly,
I am doing it on his behalf.


Modules to be used in the following order:

1. FilterPackets.py : Take inputdir or input files from PCAPFILES.
The module runs tshark on each file in inputdir and extracts the
fields mention in TsharkOptions.txt such as src-ip,dst-ip,
protocol, payload length. One new file is created per pcap file 
which contains only the fields we want for future analysis. The
new files are stored in PCAPDATADIR.

usage : python FilterPackets.py

2. GenerateFlows.py : Take each file from PCAPDATADIR -> generate
flow information -> store processed data for each file in
FLOWDATADIR. 

usage : python GenerateFlows.py

3. generateSuperFlows.py : Take each file from FLOWDATADIR -> merge
flows into superflows based on input parameters -> store in 
SUPERFLOWDATADIR.

usage: python generateSuperFlows.py start(in hrs) increment(in hrs) end(in hrs)

Number of files generated = (end - start)/increment
One file is generated for each value of timegap ranging from start to end.

4. plotGraphs.py: for generating graphs

5. createTrainingData.py: use this file to create labelled training data set. 
It reads *folders* (not files) residing in SUPERFLOWDATADIR, and creates *one* 
labelled file (weka style minus the header) per folder (with required attributes only- 
no. of pkts, no. of bytes, iat, duration, label) with the folder name appended as last column.
