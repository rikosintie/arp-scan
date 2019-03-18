# arp-scan
Creates several arp-scan commands to help locate an unused IP address on a LAN or locate a device patched on a port that is configured on the wrong vlan.

The commands are executed from the script and the results returned to the screen. Arp is a layer 2 protocol so you the subnet you enter must be on the same vlan as the port you are connected to. The advantage to using arp over ICMP is that devices with firewalls may not reply to ICMP but they should reply to arp. 

The Menu item 2 is different. It is designed to arp devices that got patched back in wrong during a cutover and now don't respond to ping. To use this script you must be connected to a trunk port that allows tagged traffic on the vlan the device is configured for. Since this is a layer two protocol you don't need a valid IP address on your laptop.

See 
https://mwhubbard.blogspot.com/2017/04/using-arp-scan-to-find-free-ip-address.html 

and

https://mwhubbard.blogspot.com/2019/02/locate-ip-devices-on-wrong-vlan.html

for detailed instructions.

On *nix systems use ```python3 arpscan.py``` to execute

You may have to install arp-scan on your system using your package manager. 
If your distro doesn't have arp-scan you can download it from [Roy Hill's Github](https://github.com/royhills/arp-scan)

If you create a file "ip.txt" in the folder where you run the script it will load the 
IP address as a default and use it where an ip address is needed. The file should have one 
line - the ip address or netork and mask (Ex. 192.168.10.0/24) to use.

Usage
```
Look for an open IP address.
Script usage
0 Initial arp-scan output
1 Enter two unused IP addresses
2 Scan for a lost device

Input a number to select 0
Enter an IP Address or network - use /24 style mask: [192.168.10.0/24]: 
Enter an interface name if needed: wlp0s20f3


*****************************************************************

sudo arp-scan -I wlp0s20f3 --arpspa=127.0.0.1 192.168.10.0/24
Interface: wlp0s20f3, datalink type: EN10MB (Ethernet)
Starting arp-scan 1.9 with 256 hosts (http://www.nta-monitor.com/tools/arp-scan/)
192.168.10.13    64:52:99:69:fd:20    The Chamberlain Group, Inc
.
. Output removed
.
192.168.10.174	f0:76:6f:71:4b:10	Apple, Inc.

23 packets received by filter, 0 packets dropped by kernel
Ending arp-scan 1.9: 256 hosts scanned in 2.011 seconds (127.30 hosts/sec). 22 responded

*****************************************************************

Script usage
0 Initial arp-scan output
1 Enter two unused IP addresses
2 Scan for a lost device

Input a number to select 1
Enter the 1st IP Address 192.168.10.15
Enter the 2nd IP Address 192.168.10.16
Enter an interface name if needed wlp0s20f3

*****************************************************************
sudo arp-scan -I wlp0s20f3 --arpspa=192.168.10.15 192.168.10.16
sudo arp-scan -I wlp0s20f3 --arpspa=192.168.10.16 192.168.10.15
*****************************************************************

[sudo] password for mhubbard: 
Interface: wlp0s20f3, datalink type: EN10MB (Ethernet)
Starting arp-scan 1.9 with 1 hosts (http://www.nta-monitor.com/tools/arp-scan/)

0 packets received by filter, 0 packets dropped by kernel
Ending arp-scan 1.9: 1 hosts scanned in 1.480 seconds (0.68 hosts/sec). 0 responded
Interface: wlp0s20f3, datalink type: EN10MB (Ethernet)
Starting arp-scan 1.9 with 1 hosts (http://www.nta-monitor.com/tools/arp-scan/)

0 packets received by filter, 0 packets dropped by kernel
Ending arp-scan 1.9: 1 hosts scanned in 1.440 seconds (0.69 hosts/sec). 0 responded

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

Look for a missing device
Script usage
0 Initial arp-scan output
1 Enter two unused IP addresses
2 Scan for a lost device

Input a number to select 2
Enter the vlan ID: 46
Enter the MAC Address: 34:64:a9:03:93:f1
Enter the IP Subnet: 10.112.100.0/24
Enter an interface: wlp0s20f3

IP Subnet 10.112.100.0/24
*****************************************************************
To re-run copy/paste this line:
sudo arp-scan -I enp2s0f1 -Q 46 --destaddr=00:90:9e:9a:b5:3d 10.112.100.0/24

 sudo arp-scan -I enp2s0f1 -Q 46 --destaddr=00:90:9e:9a:b5:3d 10.112.100.0/24
WARNING: Could not obtain IP address for interface enp2s0f1. Using 0.0.0.0 for
the source address, which is probably not what you want.
Either configure enp2s0f1 with an IP address, or manually specify the address
with the --arpspa option.
Interface: enp2s0f1, datalink type: EN10MB (Ethernet)
Starting arp-scan 1.9 with 256 hosts (http://www.nta-monitor.com/tools/arp-scan/)
10.112.100.1    00:90:9e:9a:b5:3d    Critical IO, LLC (802.1Q VLAN=46)

1 packets received by filter, 0 packets dropped by kernel
Ending arp-scan 1.9: 256 hosts scanned in 2.556 seconds (100.16 hosts/sec). 1 responded

***************************************************************** 

You can see that arp-scan found the device by mac address and the device replied with its IP address and that the laptop didn't have an address.
```
