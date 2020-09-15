for i in $(seq 1 1059);do
	sudo tshark -nr MarketDump.pcapng -z follow,tcp,ascii,$i | awk '/Follow:/,/===/'>>out.txt;
done
