for ip in $(seq 1 5);do ping -c 1 172.19.0.$ip >> /dev/null && echo "online 172.19.0.$ip";done

prot scan:

for port in 22 25 80 443 8080;do (echo gg > /dev/tcp/172.19.0.2/$port && echo "port -$port") 2>/dev/null; done


all port scan:

for port in $(seq 1 65535);do (echo gg > /dev/tcp/172.19.0.2/$port && echo "port -$port") 2>/dev/null; done
