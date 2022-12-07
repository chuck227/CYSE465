import velodyne_decoder as vd

config = vd.Config(model="VLP-16", rpm=600)
pcap_file = 'attack.pcap'
cloud_arrays = []
testFile = open("TEST", 'wb')
for stamp, points in vd.read_pcap(pcap_file, config):
    cloud_arrays.append(points)
    print(cloud_arrays)
    #print(bytes(cloud_arrays[0][0][0]))
#    testFile.write(cloud_arrays)
    exit()
