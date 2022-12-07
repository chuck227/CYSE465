from scapy.all import *
import os

packet_count = 0

def random_data(packet):
    global packet_count
    if packet_count >= 75000:
        data = packet[Raw].load
        data = bytearray(os.urandom(len(data)))
        packet[Raw].load = data
    if packet_count >= 125000:
        exit()
    wrpcap("corrupt_data_simple.pcap", packet, append=True)
    packet_count += 1

clearer = open("corrupt_data_simple.pcap", 'w')
clearer.close()

pcap_file = sys.argv[1]
sniff(offline=pcap_file, prn=random_data)
