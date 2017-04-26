# https://github.com/royhills/arp-scan
# https://www.blackmoreops.com/2015/12/31/use-arp-scan-to-find-hidden-devices-in-your-network/
# http://pentestmonkey.net/blog/the-science-of-safely-finding-an-unused-ip-address
#written in Python 3.4.4
#version is printed out on the output
#If you receive "File "<string>", line 1" when running look at the version information printed.
#If it shows other than 3.4 use "python nmap3.py"
#once you select a number you will be asked for an IP address. Network and /mask works also.
#The script will output the appropriate arp-scan command. 

print('''
*********************************************************************************
Find an unused IP address on the LAN. You my need to use Wireshark
initally to find some addresses in use on the LAN.

The script creates several arp-scan commands. These scans will find devices 
that don't respond to ping. Once arp-scan finishes pick two unused addresses
at the top and bottom of the range. 

Rerun the script selecting 1. Enter the two IP addresses. The script will 
output two more arp-scan commands. Run these to verify that the two IPs really
aren't in use. 
**********************************************************************************


''')

import sys; print(sys.version)

print()

print('Usage')
print ('0 Initial arp-scan output')
print('1 Enter two unused IP addresses')


scanTest=int(input('Input a number to select '))

if scanTest == 0:
# 0 Enter the network and mask to scan Ex. 10.140.100.0/24
	IPAddress=input('Enter the IP Address ')
	interface=input('Enter an interface name if needed ')
	if not interface:
		interface = ''
	else: 
		interface ='-I ' + interface	
	print('sudo arp-scan',interface, '--arpspa=127.0.0.1',IPAddress)
	print('sudo arp-scan',interface, '--arpspa=0.0.0.0',IPAddress)
	print('sudo arp-scan',interface, '--arpspa=255.255.255.255',IPAddress)
	print('sudo arp-scan',interface, '--arpspa=1.0.0.1',IPAddress)

elif scanTest == 1:
# 1 Enter the two IP addresses to test
	IPAddress=input('Enter the 1st IP Address ')
	IPAddress1=input('Enter the 2nd IP Address ')
	print('sudo arp-scan interface --arpspa=',IPAddress, IPAddress1)
	print('sudo arp-scan interface --arpspa=',IPAddress1, IPAddress)
	