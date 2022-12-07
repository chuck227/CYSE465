from scapy.all import *
import os

packet_count = 0

def random_data(packet):
    global packet_count
    if UDP not in packet:
        return
    if (packet[UDP].dport != 2368 and packet[UDP].dport != 2369):
        return
    if packet_count % 1000 == 0:
        print(packet_count)
    if packet_count >= 75000:
        print("corrupt")
        data = packet[Raw].load
        data = data[:2] + bytearray(os.urandom(len(data)-2))
        packet[Raw].load = data
    if packet_count >= 125000:
        exit()
    
    wrpcap("corrupt_data_live.pcap", packet, append=True)
    packet_count += 1

clearer = open("corrupt_data_live.pcap", 'w')
clearer.close()

# pcap_file = sys.argv[1]
sniff(prn=random_data, iface="lo")
