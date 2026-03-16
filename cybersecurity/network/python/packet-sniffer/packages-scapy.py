from scapy.all import *


hosts = ["google.com"]


pacote = IP(dst=hosts)/TCP(dport=(1,500), flags="S")
respondidos, nao_respondidos = sr(pacote, timeout=1)
for n in range(len(respondidos)):
	print("{} -> {}".format(respondidos[n][0][IP].dst, respondidos[n][0][TCP].dport))
