import re

arp = "22.22.22.1   0   b4:a9:5a:ff:c8:45 VLAN#222       L"

SUS = re.search(r"(.+?)  +(\d)  +(.+?)\s{2,}(\w)*", arp)
print(SUS.group(1))

SUS = re.search(r"(.+) +(\d) +(.+?)\s{2,}(\w)*", arp)
print(SUS.group(1))

print(SUS.group(2))

while True:
    input("[ $ ] ")
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
