import json

# read data from the JSON file
with open('sample-data.json') as f:
    data = json.load(f)

# print the data as a Python object
print(data)

import json

# read data from the JSON file
with open('sample-data.json') as f:
    data = json.load(f)

# print the header
print("Interface Status")
print("=" * 80)
print("DN".ljust(50) + "Description".ljust(25) + "Speed".ljust(8) + "MTU")
print("-" * 80)

# print the interface status
for interface in data['imdata']:
    dn = interface['l1PhysIf']['attributes']['dn']
    descr = interface['l1PhysIf']['attributes']['descr']
    speed = interface['l1PhysIf']['attributes']['speed']
    mtu = interface['l1PhysIf']['attributes']['mtu']
    print(dn.ljust(50) + descr.ljust(25) + speed.ljust(8) + mtu)