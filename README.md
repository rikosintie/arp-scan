# arp-scan
Creates several arp-scan commands to help locate an unused IP address on a LAN

See https://mwhubbard.blogspot.com/2017/04/using-arp-scan-to-find-free-ip-address.html for an exmaple

To execute on windows use ```python arpscan.py``` 

On Linux use ```python3 arpscan.py```

Usage
```
0 Initial arp-scan output
1 Enter two unused IP addresses
Input a number to select 0
Enter the IP Address 192.168.10.0/24
Enter an interface name if needed wlan1
sudo arp-scan -I wlan1 --arpspa=127.0.0.1 192.168.10.0/24
sudo arp-scan -I wlan1 --arpspa=0.0.0.0 192.168.10.0/24
sudo arp-scan -I wlan1 --arpspa=255.255.255.255 192.168.10.0/24
sudo arp-scan -I wlan1 --arpspa=1.0.0.1 192.168.10.0/24


0 Initial arp-scan output
1 Enter two unused IP addresses
Input a number to select 1
Enter the 1st IP Address 192.168.10.10
Enter the 2nd IP Address 192.168.10.240
sudo arp-scan interface --arpspa= 192.168.10.10 192.168.10.240
sudo arp-scan interface --arpspa= 192.168.10.240 192.168.10.10
```
