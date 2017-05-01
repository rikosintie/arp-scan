# arp-scan
Creates several arp-scan commands to help locate an unused IP address on a LAN

The commands are executed from the script and the results returned to the screen.

See https://mwhubbard.blogspot.com/2017/04/using-arp-scan-to-find-free-ip-address.html for an exmaple

On *nix systems use ```python3 arpscan.py``` to execute

Usage
```
Script usage
0 Initial arp-scan output
1 Enter two unused IP addresses
Input a number to select 0
Enter a single IP Address or network - use /24 style mask: 192.168.10.0/24
Enter an interface name if needed: eth0


*****************************************************************

sudo arp-scan eth0 --arpspa=127.0.0.1 192.168.10.0/24
Interface: eth0, datalink type: EN10MB (Ethernet)
Starting arp-scan 1.8.1 with 256 hosts (http://www.nta-monitor.com/tools/arp-scan/)
192.168.10.13	64:52:99:69:fd:20	(Unknown)
192.168.10.20	c0:3f:d5:68:0c:cc	(Unknown)
192.168.10.167	b8:78:2e:08:28:05	(Unknown)

3 packets received by filter, 0 packets dropped by kernel
Ending arp-scan 1.8.1: 256 hosts scanned in 1.350 seconds (189.63 hosts/sec). 3 responded


*****************************************************************

```
