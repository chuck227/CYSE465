Contribution: Was the primary coder, and researcher for the project. Recorded the demo video as well.

There are a two attacks run from scripts in this repo. The first is attackOutput_simple.py. This creates a pcap which can be replayed through udpreplay where the data has been corrupted. It can be run with python3 attackOutput_simple.py and then specify the name of the pcap. The other is attackOutput.py which is very similar to the previous except this attack, has packets which are authenticateed to the sensors even though the data has been corrupted. It can be run with python3 attackOutput.py and then specify the pcap to attack.

Demo Video: https://youtu.be/REMBaZ0vu2M
