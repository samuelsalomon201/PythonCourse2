arp = "22.22.22.1      0       b4:a9:5a:ff:c8:45 VLAN#222      L"

import re

WAA = re.findall(r"\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}, arp")

print(WAA)
print(type(WAA))
