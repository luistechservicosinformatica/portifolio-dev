from scapy.all import *




def print_pacote(pkt):
	data_pkt = raw(pkt[TCP].payload).decode("latin-1")
	print(data_pkt)




pacote = sniff(filter="tcp", prn=print_pacote, store=0)
