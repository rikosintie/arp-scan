'''
https://github.com/royhills/arp-scan
https://www.blackmoreops.com/2015/12/31/use-arp-scan-to-find-hidden-devices-in-your-network/
http://pentestmonkey.net/blog/the-science-of-safely-finding-an-unused-ip-address
written in Python 3.6.0
Your Python version is printed out at the beging of the script
If you receive "File "<string>", line 1" when running look at the version information printed.
If it shows other than 3.4 use "python nmap3.py"
once you select a number you will be asked for an IP address. Network and /mask works also.
The script will output the appropriate arp-scan command. 
subprocess.run(["sudo", "arp-scan", "-I", "eth2", "--arpspa=127.0.0.1", "10.112.39.0/24"])
'''

print()
import subprocess
import sys
import re
ver =  sys.version
pattern = re.compile('\A\d{1}.{1}\d{1}.{1}\d{1}.{1}')
ver = re.findall(pattern,ver)
print()
ver = ver[0]
print('Running Python version ----> %s' %(ver))

print('''
********************************************************************************************
arp-scan is a layer 2 tool. You must be connected to the LAN or vlan that you are scanning. 
If you run arp-scan manually you can pass vlan tags. I plan to add that to the script in 
the future.

This script finds an unused IP address on the LAN. You may need to use Wireshark initally to 
find some addresses in use on the LAN. Set the display filter to arp and what a few minutes.

The script creates several arp-scan commands. These scans will find devices that don't 
respond to ping. Once arp-scan finishes pick two unused addresses at the top and bottom of 
the range. 

Rerun the script selecting 1. Enter the two IP addresses. The script will output two more 
arp-scan commands. Run these to verify that the two IPs really aren't in use. 

If you create a file "arpscan.txt" in the folder where you run the script it will load the 
IP address as a default and use it where an ip address is needed. The file should have one 
line - the ip address or netork and mask (Ex. 192.168.10.0/24) to use.
********************************************************************************************
''')

def readip():
    """
    create a file named arpscan.txt in the folder where the script is executed.
    In the file enter one ip address or ip address range compatable with
    nmap. 

    The script will read the file and insert the ip address when 
    prompting for an ip address. Simply hit [Enter] to accept the IP. 
    You can override the default by typing in an address.
    This allows you to quickly run several different scans with the same
    IP address.
    """

    try:
        IP = []
        f = open('arpscan.txt', 'r')
        for line in f:
            IP.append(line)
        f.close
    except: # FileNotFoundError:
        IPAddress = input('Enter a single IP Address or network - use /24 style mask: ')
        return IPAddress  

    try:
	    ipsaved = IP[0]
	    ipsaved = ipsaved.strip('\n')
	    if not ipsaved:
	        IPAddress = input('Enter a single IP Address or network - use /24 style mask: ')
	    else:
	        IPAddress = input('Enter a single IP Address or network - use /24 style mask: [%s]: ' %(ipsaved))
	    if not IPAddress:
	        IPAddress = ipsaved

	    return IPAddress  
    except:
        print('\n[!] An Unknown Error Occured or CTRL+C was pressed')


print()
print('Script usage')
print('0 Initial arp-scan output')
print('1 Enter two unused IP addresses')


#scanTest = input('Input a number to select ')

#Make sure 0 or 1 was entered
scanTest = False
try:
	while (scanTest != '0') and (scanTest != '1'):
		scanTest = input('Input a number to select ')
except: # if ctrl+c is pressed exit gracefully
	print('\n[!] An Unknown Error Occured or CTRL+C was pressed')
	raise SystemExit

scanTest = int(scanTest)

if scanTest == 0:
# 0 Enter the network and mask to scan Ex. 10.140.100.0/24
	IPAddress = readip()
#	IPAddress=input('Enter a single IP Address or network - use /24 style mask: ')
	interface=input('Enter an interface name if needed: ')
#	if not interface:
#
#	else: 
#		interface ='-I ' + interface
#		I = '-I'
	print()
	print()
	print('*' * 65)	
	print()
	if not interface:
		print('sudo arp-scan --arpspa=127.0.0.1',IPAddress)
		subprocess.run(['sudo', 'arp-scan', '--arpspa=127.0.0.1',IPAddress])
	else:
		I = '-I'
		print('sudo arp-scan',interface, '--arpspa=127.0.0.1',IPAddress)
		subprocess.run(['sudo', 'arp-scan',I,interface, '--arpspa=127.0.0.1',IPAddress])
	print()
	print()	
	print('*' * 65)
	print()
	if not interface:
		print('sudo arp-scan --arpspa=0.0.0.0',IPAddress)
		subprocess.run(['sudo', 'arp-scan', '--arpspa=0.0.0.0',IPAddress])
	else:
		I = '-I'
		print('sudo arp-scan',interface, '--arpspa=0.0.0.0',IPAddress)
		subprocess.run(['sudo', 'arp-scan',I,interface, '--arpspa=0.0.0.0',IPAddress])
	print()
	print()
	print('*' * 65)
	print()	
	if not interface:
		print('sudo arp-scan --arpspa=255.255.255.255',IPAddress)
		subprocess.run(['sudo', 'arp-scan', '--arpspa=255.255.255.255',IPAddress])
	else:
		I = '-I'
		print('sudo arp-scan',interface, '--arpspa=255.255.255.255',IPAddress)
		subprocess.run(['sudo', 'arp-scan',I,interface, '--arpspa=255.255.255.255',IPAddress])
	print()
	print()
	print('*' * 65)
	print()
	if not interface:
		print('sudo arp-scan --arpspa=1.0.0.1',IPAddress)
		subprocess.run(['sudo', 'arp-scan', '--arpspa=1.0.0.1',IPAddress])
	else:
		I = '-I'
		print('sudo arp-scan',interface, '--arpspa=1.0.0.1',IPAddress)
		subprocess.run(['sudo', 'arp-scan',I,interface, '--arpspa=1.0.0.1',IPAddress])
	print()
	print()
	print('*' * 65)
	

elif scanTest == 1:
# 1 Enter the two IP addresses to test
	IPAddress=input('Enter the 1st IP Address ')
	IPAddress1=input('Enter the 2nd IP Address ')
	interface=input('Enter an interface name if needed ')
#print some space 
	print()
	print()
	print('*' * 65)	
#If no interface is entered
	if not interface:
		print('sudo arp-scan --arpspa='+IPAddress, IPAddress1)
		print('sudo arp-scan --arpspa='+IPAddress1, IPAddress)
		arp = '--arpspa=' + IPAddress
		arp1 = '--arpspa=' + IPAddress
		subprocess.run(['sudo', 'arp-scan', arp, IPAddress1])
		subprocess.run(['sudo', 'arp-scan', arp1, IPAddress])
#If an interface is entered
	else: 
		I ='-I'
		arp = '--arpspa=' + IPAddress
		arp1 = '--arpspa=' + IPAddress1
#		print('I:', I)
#		print('interface:', interface)
#		print('arp:', arp)
#		print('arp1:', arp1)
		print('sudo arp-scan',I,interface, '--arpspa='+IPAddress, IPAddress1)
		print('sudo arp-scan',I,interface, '--arpspa='+IPAddress1, IPAddress)
		print('*' * 65)	
		print()
		subprocess.run(['sudo', 'arp-scan',I,interface, arp, IPAddress1])
		subprocess.run(['sudo', 'arp-scan',I,interface, arp1, IPAddress])
	print()
	print('*' * 65)
	print()
